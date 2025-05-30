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

    # Flexible degree extraction
    match = re.match(r"(.*?)(Masters|PhD|MFA|MA|MS|MBA|Other|JD|MD)?\.?$", program_degree, re.IGNORECASE)
    program = match.group(1).strip() if match else program_degree
    degree = match.group(2) if match and match.group(2) else "Unknown"

    # Extract result link from last td (typically contains the /result/ link)
    more_info_link = "None"
    if len(td_tags) == 5:
        link_tag = td_tags[4].find("a", href=re.compile(r"^/result/\d+"))
        if link_tag and link_tag["href"]:
            more_info_link = "https://www.thegradcafe.com" + link_tag["href"]

    # Default "None" values for optional fields
    semester = gre = gre_v = gre_aw = gpa = applicant_type = comments = "None"

    if detail_tr:
        detail_td = detail_tr.find("td")
        if detail_td:
            detail_text = detail_td.get_text(" ", strip=True)

            # Extract structured fields using regex
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
            applicant_type = applicant_match.group(1) if applicant_match else "None"

            # Extract comments from <p> tags if present
            p_tags = detail_td.find_all("p")
            if p_tags:
                comments = " ".join(p.get_text(strip=True) for p in p_tags)

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
        "International/American Student": applicant_type,
        "Comments": comments,
        "More Info Link": more_info_link
    }