from bs4 import BeautifulSoup
import re

def clean_data(main_tr, detail_tr=None, entry_number=1):
    td_tags = main_tr.find_all("td")
    td_values = [td.get_text(strip=True) for td in td_tags]

    if len(td_values) < 3:
        return None

    institution = td_values[0]
    program_degree = td_values[1]
    date_added = td_values[2]
    decision = td_values[3] if len(td_values) > 3 else "None"

    # Degree parsing
    match = re.match(r"(.*?)(Masters|PhD|MFA|MA|MS|MBA|Other|JD|MD)?\.?$", program_degree, re.IGNORECASE)
    program = match.group(1).strip() if match else program_degree
    degree = match.group(2) if match and match.group(2) else "Unknown"

    # Defaults
    semester = gre = gre_v = gre_aw = gpa = applicant_status = comments = "None"

    if detail_tr:
        detail_td = detail_tr.find("td")
        if detail_td:
            detail_text = detail_td.get_text(" ", strip=True)

            semester_match = re.search(r"(Fall|Spring|Summer|Winter) \d{4}", detail_text)
            gpa_match = re.search(r"GPA[: ]?(\d\.\d+)", detail_text)
            gre_match = re.search(r"\bGRE[: ]?(\d{2,3})\b", detail_text)
            gre_v_match = re.search(r"\bGRE V[: ]?(\d{2,3})\b", detail_text)
            gre_aw_match = re.search(r"\bGRE AW[: ]?(\d(?:\.\d{1,2})?)\b", detail_text)
            applicant_match = re.search(r"(International|American)", detail_text)

            semester = semester_match.group(0) if semester_match else "None"
            gpa = gpa_match.group(1) if gpa_match else "None"
            gre = gre_match.group(1) if gre_match else "None"
            gre_v = gre_v_match.group(1) if gre_v_match else "None"
            gre_aw = gre_aw_match.group(1) if gre_aw_match else "None"
            applicant_status = applicant_match.group(1) if applicant_match else "None"

            # ✅ Extract all <p> tag comments from the entire detail row
            if detail_tr and detail_tr.find_next_sibling("tr"):
                possible_comment_tr = detail_tr.find_next_sibling("tr")
                if possible_comment_tr:
                    comment_td = possible_comment_tr.find("td")
                    if comment_td:
                        comment_p = comment_td.find("p")
                        if comment_p:
                            comments = comment_p.get_text(strip=True)


    # Extract link to more info
    more_info_link = "None"
    if len(td_tags) == 5:
        link_tag = td_tags[4].find("a", href=re.compile(r"^/result/\d+"))
        if link_tag and link_tag["href"]:
            more_info_link = "https://www.thegradcafe.com" + link_tag["href"]

    return {
        "Entry": entry_number,
        "Institution": institution,
        "Program": program,
        "Degree": degree,
        "Decision": decision,
        "Date Added": date_added,
        "Semester": semester,
        "GPA": gpa,
        "GRE": gre,
        "GRE V": gre_v,
        "GRE AW": gre_aw,
        "International/American Student": applicant_status,
        "Comments": comments,
        "More Info Link": more_info_link
    }