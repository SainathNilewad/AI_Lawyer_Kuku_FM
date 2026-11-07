"""
legal_kb.py - Verified Indian Statutory Knowledge Base for Everyday Legal Disputes
Authoritative knowledge base covering:
1. Tenancy & Rental Disputes (Model Tenancy Act, Transfer of Property Act Sec 108)
2. Consumer Protection & E-Commerce Grievances (Consumer Protection Act 2019, e-Daakhil)
3. Employment & Labor Disputes (Code on Wages, 2019)
4. Civil vs. Criminal Escalation Guardrails (Civil Breach vs. Criminal Intent)
"""

from typing import List, Dict, Any, Set
import re

# Curated statutory entries for everyday Indian disputes
# Every entry carries a source_url, verified_on date, and verification status.
VERIFIED_STATUTORY_DATABASE: List[Dict[str, Any]] = [
    # ==================== TENANCY & RENTAL DISPUTES ====================
    {
        "domain": "Tenancy & Rental",
        "act": "Model Tenancy Act, 2021 (and State Rent Control Enactments)",
        "source_url": "https://mohua.gov.in/",
        "verified_on": "2026-11-07",
        "status": "verified",
        "sections": ["Section 12", "Section 13", "Section 13(1)", "Section 13(2)", "Section 14", "Section 21", "Section 21(1)", "Section 21(2)"],
        "key_provisions": (
            "1. Note on Enforceability: The Model Tenancy Act, 2021 is a central model law drafted by the Ministry of Housing and Urban Affairs "
            "under Entry 18 of the State List and binds only States and Union Territories that formally adopt or enact it (such as Andhra Pradesh, "
            "Uttar Pradesh, Tamil Nadu, and Assam which have enacted aligned tenancy legislations). Other states (e.g. Karnataka, Maharashtra, Delhi) "
            "continue under their respective State Rent Control Acts alongside Section 108 of the Transfer of Property Act, 1882.\n"
            "2. Retention of Tenancy Agreement (Section 12): The tenancy agreement shall be signed in duplicate by both the landlord and tenant, "
            "and one each of such original signed tenancy agreement shall be retained by the landlord and tenant.\n"
            "3. Rent Payment and Conclusive Proof (Section 13): Every tenant shall pay rent within the agreed period (sub-section (1)). "
            "The landlord must forthwith provide a duly signed receipt against acknowledgement (sub-section (2)). "
            "Crucially, the proviso to Section 13(2) provides that where payment of rent or other charges is made through electronic mode, "
            "the bank acknowledgment thereof shall be conclusive proof of such payment.\n"
            "4. Deposit of Rent with Rent Authority (Section 14): Where the landlord refuses to accept rent or refuses to give a receipt, "
            "the rent may be paid by money order consecutively for two months, and if still refused, the tenant may deposit the same with the Rent Authority.\n"
            "5. Protection Against Eviction (Section 21): Under Section 21(1), a tenant shall not be evicted during the continuance of the tenancy agreement "
            "except in accordance with an order of the Rent Court on specified grounds under Section 21(2) (e.g. non-payment of rent arrears for 2 consecutive months, "
            "subletting without written consent, misuse causing public nuisance or property damage, or unauthorized structural changes).\n"
            "6. Security Deposit Cap (Statutory Note): Residential security deposit caps (up to 2 months' rent) derive from Section 11 of the Model Act "
            "and applicable state adoption enactments."
        ),
        "remedy_steps": [
            "Produce electronic bank / UPI transfer statement as conclusive proof of rent payment under proviso to Section 13(2).",
            "Serve a formal written legal notice citing Section 21(1) against unlawful eviction or Section 108(B)(m) for deposit recovery.",
            "If unresolved, file an application before the local Rent Authority / Rent Court (subject to state adoption)."
        ]
    },
    {
        "domain": "Tenancy & Rental",
        "act": "Transfer of Property Act, 1882",
        "source_url": "https://www.indiacode.nic.in/",
        "verified_on": "2026-11-07",
        "status": "verified",
        "sections": ["Section 108(B)(m)", "Section 108(B)(q)", "Section 108(B)(f)", "Section 108(A)(c)"],
        "key_provisions": (
            "1. Reasonable Wear and Tear (Section 108(B)(m)): The lessee is bound to keep, and on the determination of the lease to restore, "
            "the property in as good condition as it was in at the time when he was put in possession, "
            "'subject only to the changes caused by reasonable wear and tear or irresistible force'. "
            "[Interpretation: Routine paint aging, minor nail holes, or normal weathering constitute reasonable wear and tear under this clause].\n"
            "2. Handover of Possession (Section 108(B)(q)): On the determination of the lease, the lessee is bound to put the lessor into possession of the property.\n"
            "3. Necessary Repairs (Section 108(B)(f)): Under Section 108(B) (rights of the lessee), if the lessor neglects to make, "
            "within a reasonable time after notice, any repairs which he is bound to make to the property, "
            "the lessee may make the same himself, and deduct the expense of such repairs with interest from the rent, or otherwise recover it from the lessor.\n"
            "4. Quiet Enjoyment (Section 108(A)(c)): Under Section 108(A) (rights and liabilities of the lessor), the lessor shall be deemed to contract "
            "with the lessee that, if the latter pays the rent reserved by the lease and performs lease contracts, he may hold the property during the lease term without interruption."
        ),
        "remedy_steps": [
            "Serve a 15-day formal Legal Demand Notice citing Section 108(B)(m) demanding full refund of unlawfully deducted deposit amounts.",
            "If unresolved, file a recovery suit before the local civil court / Small Causes Court."
        ]
    },

    # ==================== CONSUMER & E-COMMERCE DISPUTES ====================
    {
        "domain": "Consumer Protection",
        "act": "Consumer Protection Act, 2019 (CPA 2019)",
        "source_url": "https://www.indiacode.nic.in/",
        "verified_on": "2026-11-07",
        "status": "verified",
        "sections": ["Section 2(7)", "Section 2(10)", "Section 2(11)", "Section 2(47)", "Section 35", "Section 84"],
        "key_provisions": (
            "1. Consumer Definition (Section 2(7)): Any person buying goods or hiring services for consideration; "
            "expressly includes online/e-commerce transactions (Explanation (b)). Excludes commercial resale, but covers self-employment livelihood.\n"
            "2. Defect in Goods (Section 2(10)): Any fault, imperfection, or shortcoming in the quality, quantity, potency, purity or standard "
            "which is required to be maintained by or under any law for the time being in force or under any contract, express or implied, "
            "or as is claimed by the trader in any manner whatsoever in relation to any goods or product.\n"
            "3. Deficiency in Service (Section 2(11)): 'deficiency' means any fault, imperfection, shortcoming or inadequacy "
            "in the quality, nature and manner of performance which is required to be maintained by or under any law for the time being in force "
            "or has been undertaken to be performed by a person in pursuance of a contract or otherwise in relation to any service, and includes: "
            "(i) any act of negligence or omission or commission which causes loss or injury to the consumer, and "
            "(ii) deliberate withholding of relevant information to the consumer.\n"
            "4. Unfair Trade Practice (Section 2(47)): Deceptive practices including falsely representing second-hand goods as new (sub-clause (i)(c)), "
            "misleading repair/replacement promises without reasonable prospect of fulfillment (sub-clause (i)(h)), and refusing to refund consideration "
            "for defective goods or deficient services within the period stipulated in the bill/cash memo or, in the absence of stipulation, "
            "within a period of thirty days (sub-clause (viii)).\n"
            "5. Liability of Product Manufacturer (Section 84): A product manufacturer shall be liable in a product liability action if the product: "
            "(a) contains a manufacturing defect, (b) is defective in design, (c) deviates from manufacturing specifications, "
            "(d) does not conform to the express warranty, or (e) fails to contain adequate instructions/warnings to prevent harm; "
            "and under sub-section (2), is liable even if proving absence of negligence or fraud in making the express warranty.\n"
            "6. Filing of Complaint (Section 35): Manner of filing a consumer complaint before the District Commission; "
            "the proviso to Section 35(1) explicitly provides that 'the complaint may also be filed electronically in such manner as may be prescribed' "
            "(statutory basis for electronic filing on e-Daakhil)."
        ),
        "remedy_steps": [
            "Lodge formal complaint on National Consumer Helpline (NCH) toll-free 1915 or consumerhelpline.gov.in.",
            "Serve a 15-day formal Legal Demand Notice to the seller and e-commerce platform.",
            "File an electronic consumer complaint online on e-Daakhil (edaakhil.nic.in) with order invoice, defect photos, and communication history."
        ]
    },

    # ==================== EMPLOYMENT & SALARY DISPUTES ====================
    {
        "domain": "Employment & Labor",
        "act": "Code on Wages, 2019",
        "source_url": "https://www.indiacode.nic.in/",
        "verified_on": "2026-11-07",
        "status": "verified",
        "sections": ["Section 17(1)", "Section 17(2)", "Section 17(4)", "Section 18(1)", "Section 18(2)", "Section 18(3)"],
        "key_provisions": (
            "1. Time Limit for Wage Payment (Section 17(1)): Wages must be paid: daily (at the end of the shift), "
            "weekly (on the last working day before the weekly holiday), fortnightly (before the end of the second day after the end of the fortnight), "
            "or monthly (before the expiry of the seventh day of the succeeding month).\n"
            "2. Payment on Removal, Dismissal or Resignation (Section 17(2)): Wages of an employee who is removed, dismissed, "
            "retrenched or resigns must be paid within two working days of that event.\n"
            "3. Other Laws Preserved (Section 17(4)): The Code does not affect any time limit for payment of wages given in any other law (state rules may differ).\n"
            "4. Authorised Deductions Only (Section 18(1), 18(2)): No deductions from wages except those authorised under Section 18(2) of the Code "
            "(e.g. fines, absence from duty, damage or loss directly attributable to neglect or default, house-accommodation, amenities, advances/loans, statutory tax/provident fund).\n"
            "5. Statutory 50% Deduction Cap (Section 18(3)): The total amount of deductions which may be made in any wage period from the wages of an employee shall not exceed fifty per cent. (50%) of such wages.\n"
            "6. Claims and Forum: Procedure and forum vary; confirm from the official text or ask a lawyer / DLSA 15100."
        ),
        "remedy_steps": [
            "Send formal written demand email to employer citing Sections 17(2) and 18(3) requesting immediate release of unpaid wages and relieving documents within statutory timelines.",
            "Procedure and forum vary; confirm from the official text or ask a lawyer / DLSA 15100."
        ]
    },

    # ==================== CIVIL VS CRIMINAL DISTINCTION ====================
    {
        "domain": "Civil vs. Criminal Boundary",
        "act": "General Legal Principle (Civil vs. Criminal Boundary)",
        "source_url": "https://www.indiacode.nic.in/",
        "verified_on": "<to be filled after check>",
        "status": "needs_my_verification",
        "sections": [],
        "key_provisions": (
            "1. Boundary Rule: Mere failure to refund a deposit, pay wages, or fulfill a contract is generally a civil dispute, not criminal cheating.\n"
            "2. Requirement for Criminal Cheating: A criminal offense typically requires proof of dishonest or fraudulent intention at the very beginning of the transaction.\n"
            "3. Warning against False Police Complaints: Filing criminal police complaints for purely civil or monetary disputes is improper and may be rejected."
        ),
        "remedy_steps": [
            "Pursue appropriate civil remedies and statutory dispute forums.",
            "Do not file criminal police complaints for purely civil disputes unless actual fraud or deception was present from inception."
        ]
    }
]

# Real Lawyer Escalation Rules (Word-beginning matching, e.g. \barrest\w*, \bassault\w*)
CRITICAL_ESCALATION_CRITERIA = [
    "cognizable violent crime",
    "arrest",
    "bail",
    "domestic violence",
    "physical harm",
    "divorce",
    "custody",
    "child maintenance",
    "spousal maintenance",
    "alimony",
    "writ petition",
    "ndps",
    "arms act",
    "sexual harassment",
    "pocso"
]

HIGH_RISK_WORDS = [
    "suicide",
    "murder",
    "assault",
    "jail",
    "police custody",
    "bribe",
    "rape",
    "weapon",
    "threat"
]

# Overriding out-of-scope topics that must REFUSE even if a civil domain also matched
OVERRIDING_OUT_OF_SCOPE_TOPICS = [
    "divorce",
    "custody",
    "child maintenance",
    "spousal maintenance",
    "alimony",
    "writ petition"
]

# Domain keyword lists (strictly whole-word matched, generic words removed)
TENANCY_KEYWORDS = ["rent", "rental", "landlord", "tenant", "deposit", "flat", "lease", "evict", "broker"]
CONSUMER_KEYWORDS = ["refund", "product", "defective", "flipkart", "amazon", "seller", "warranty", "ecommerce", "consumer", "service", "repair", "replacement", "replace"]
EMPLOYMENT_KEYWORDS = ["salary", "employer", "resignation", "relieving", "wages", "terminated", "fnf", "dues"]

def _matches_any_whole_word(text: str, keywords: List[str]) -> bool:
    """Matches keywords as whole words only to prevent false substring triggers."""
    return any(re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE) for kw in keywords)

def _matches_word_beginning(pattern_phrase: str, text: str) -> bool:
    """
    Matches word beginnings using regex word boundary and word character extensions.
    Example: 'arrest' matches 'arrest', 'arrested', 'arresting'.
    Example: 'assault' matches 'assault', 'assaulted'.
    Example: 'writ petition' matches 'writ petition', 'writ petitions'.
    """
    pattern_phrase = pattern_phrase.strip()
    if not pattern_phrase:
        return False
    if " " in pattern_phrase:
        parts = pattern_phrase.split()
        regex_parts = [r'\b' + re.escape(p) + (r'\w*' if i == len(parts) - 1 else r'\w*\s+') for i, p in enumerate(parts)]
        regex_str = "".join(regex_parts)
    else:
        regex_str = r'\b' + re.escape(pattern_phrase) + r'\w*'
    return bool(re.search(regex_str, text, re.IGNORECASE))

def retrieve_verified_legal_context(query: str, domain_filter: str = None) -> Dict[str, Any]:
    """
    Deterministically retrieves verified statutory provisions.
    Uses whole-word matching and excludes generic terms.
    If overriding out-of-scope topics match, REFUSES even if a civil domain also matched.
    If no domain matches, returns an explicit out-of-scope fallback (no guessing).
    """
    query_str = str(query or "")

    # Overriding out-of-scope check: REFUSE even if a civil domain also matched
    for topic in OVERRIDING_OUT_OF_SCOPE_TOPICS:
        if _matches_word_beginning(topic, query_str):
            return {
                "matched_count": 0,
                "entries": [],
                "out_of_scope": True,
                "refusal_reason": f"Topic '{topic}' is outside covered everyday civil domains (family law / writ jurisdiction).",
                "grounding_text": (
                    "OUT_OF_SCOPE: This query touches upon matters outside NyayaMitra's verified statutory domains "
                    "(Tenancy & Rental, Consumer Protection, or Code on Wages Employment). "
                    "Do NOT guess, manufacture legal principles, or invent sections. "
                    "Directly inform the user that this topic is outside what NyayaMitra covers and advise them "
                    "to consult a practicing advocate or contact the free District Legal Services Authority (DLSA) / NALSA Helpline at 15100."
                )
            }

    matched_entries = []
    
    # Check domain keywords with whole-word matching
    is_tenancy = _matches_any_whole_word(query_str, TENANCY_KEYWORDS)
    is_consumer = _matches_any_whole_word(query_str, CONSUMER_KEYWORDS)
    is_employment = _matches_any_whole_word(query_str, EMPLOYMENT_KEYWORDS)
    
    for entry in VERIFIED_STATUTORY_DATABASE:
        if is_tenancy and entry["domain"] == "Tenancy & Rental":
            matched_entries.append(entry)
        elif is_consumer and entry["domain"] == "Consumer Protection":
            matched_entries.append(entry)
        elif is_employment and entry["domain"] == "Employment & Labor":
            matched_entries.append(entry)
    
    # FIX 5: If no domain matches, DO NOT guess.
    if not matched_entries:
        return {
            "matched_count": 0,
            "entries": [],
            "out_of_scope": True,
            "grounding_text": (
                "OUT_OF_SCOPE: This query does not match any of NyayaMitra's verified statutory domains "
                "(Tenancy & Rental, Consumer Protection, or Code on Wages Employment). "
                "Do NOT guess, manufacture legal principles, or invent sections. "
                "Directly inform the user that this topic is outside what NyayaMitra covers and advise them "
                "to consult a practicing advocate or contact the free District Legal Services Authority (DLSA) / NALSA Helpline at 15100."
            )
        }

    # Include boundary entry only when a civil domain has actually matched
    for entry in VERIFIED_STATUTORY_DATABASE:
        if entry["domain"] == "Civil vs. Criminal Boundary" and entry not in matched_entries:
            matched_entries.append(entry)

    # Format into grounded text prompt
    context_str = ""
    for idx, e in enumerate(matched_entries, 1):
        context_str += f"\n--- STATUTORY GROUNDING #{idx} ---\n"
        context_str += f"Domain: {e['domain']}\n"
        context_str += f"Statute: {e['act']}\n"
        context_str += f"Status: {e.get('status', 'needs_my_verification')}\n"
        context_str += f"Source URL: {e.get('source_url', 'https://www.indiacode.nic.in/')}\n"
        context_str += f"Verified On: {e.get('verified_on', '<unverified>')}\n"
        if e.get("sections"):
            context_str += f"Applicable Sections: {', '.join(e['sections'])}\n"
        context_str += f"Key Legal Principles:\n{e['key_provisions']}\n"
        if e.get("precedents"):
            context_str += f"Authoritative Precedent: {e['precedents']}\n"
        context_str += f"Prescribed Action Steps: {'; '.join(e['remedy_steps'])}\n"

    return {
        "matched_count": len(matched_entries),
        "entries": matched_entries,
        "out_of_scope": False,
        "grounding_text": context_str
    }

def check_immediate_advocate_escalation(text: str) -> Dict[str, Any]:
    """
    Evaluates whether the user's issue goes beyond an everyday advisory AI
    and strictly requires immediate representation by a licensed advocate.
    Matches word beginnings (e.g. \\barrest\\w*, \\bassault\\w*, \\bbribe\\w*, \\bthreat\\w*).
    """
    text_str = str(text or "")
    escalation_reasons = []
    
    for trigger in CRITICAL_ESCALATION_CRITERIA:
        if _matches_word_beginning(trigger, text_str):
            escalation_reasons.append(trigger)
            
    for w in HIGH_RISK_WORDS:
        if _matches_word_beginning(w, text_str):
            escalation_reasons.append(f"High-severity issue ({w})")
        
    return {
        "requires_real_lawyer": len(escalation_reasons) > 0,
        "reasons": escalation_reasons,
        "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
    }

# ==================== FIX 4: SECTION SCANNER & GUARDRAIL ====================

def normalize_section_reference(s: str) -> str:
    """Normalizes section strings (e.g. 'Section 17(2)' -> '17(2)')."""
    s = s.strip().lower()
    s = re.sub(r'^(?:section|sec\.?|u/s)\s*', '', s)
    s = re.sub(r'\s+', '', s)
    return s

def get_allowed_sections() -> Set[str]:
    """
    Collects allowed section references ONLY from entries whose status is 'verified'.
    Includes both full clauses ('17(2)', '108(b)(m)') and parent section numbers ('17', '108').
    """
    allowed: Set[str] = set()
    for entry in VERIFIED_STATUTORY_DATABASE:
        if entry.get("status") == "verified":
            for s in entry.get("sections", []):
                norm = normalize_section_reference(s)
                if norm:
                    allowed.add(norm)
                    base = re.match(r'^([0-9]+)', norm)
                    if base:
                        allowed.add(base.group(1))
    return allowed

# Banned/repealed/unverified Act names that must never appear in AI legal outputs
BANNED_ACT_PATTERNS = [
    r"\bPayment of Wages Act(?:\s*,\s*\d{4})?\b",
    r"\bMinimum Wages Act(?:\s*,\s*\d{4})?\b",
    r"\bPayment of Bonus Act(?:\s*,\s*\d{4})?\b",
    r"\bEqual Remuneration Act(?:\s*,\s*\d{4})?\b",
    r"\bIndian Penal Code(?:\s*,\s*\d{4})?\b",
    r"\bIPC\b",
    r"\bCrPC\b",
    r"\bCode of Criminal Procedure(?:\s*,\s*\d{4})?\b",
]

def scan_banned_acts(text: str) -> List[str]:
    """Scans text for banned or repealed Act names."""
    if not text or not isinstance(text, str):
        return []
    found = []
    for pat in BANNED_ACT_PATTERNS:
        matches = re.findall(pat, text, re.IGNORECASE)
        for m in matches:
            if m not in found:
                found.append(m)
    return found

def sanitize_banned_acts(text: str) -> str:
    """Replaces banned Act names with [unverified reference removed] and logs the event."""
    if not text or not isinstance(text, str):
        return text
    banned = scan_banned_acts(text)
    if not banned:
        return text
    print(f"[SECURITY GUARD] Logged unverified Act name reference(s): {banned}")
    sanitized = text
    for pat in BANNED_ACT_PATTERNS:
        sanitized = re.sub(pat, "[unverified reference removed]", sanitized, flags=re.IGNORECASE)
    return sanitized

# Note on regex limitations (crude scanner):
# What this regex misses:
# 1. Spelled-out numbers (e.g. "Section twelve" or "Section four hundred twenty").
# 2. Roman numerals (e.g. "Section IV").
# 3. Bare numbers without section prefix (e.g. "under 420 of IPC").
# 4. Multi-section conjunctions (e.g. "Sections 12, 13 and 14" only captures 12).
# 5. Act mismatch: checks if section exists in KB, but cannot detect if an allowed section
#    from one statute is mistakenly cited under another statute.
SECTION_PATTERN = re.compile(
    r'(?i)\b(?:section|sec\.?|u/s)\s*([0-9]+(?:[\(\[][a-zA-Z0-9]+[\)\]])*(?:[a-zA-Z])*)'
)

def scan_unverified_sections(text: str) -> List[str]:
    """
    Scans an AI response for section references and returns any that are NOT in the allowed set.
    """
    if not text or not isinstance(text, str):
        return []
    allowed = get_allowed_sections()
    unverified = []
    for match in SECTION_PATTERN.finditer(text):
        raw = match.group(0)
        norm = normalize_section_reference(match.group(1))
        if norm not in allowed:
            unverified.append(raw)
    return unverified

def sanitize_unverified_sections(text: str) -> str:
    """
    Scans an AI answer for unverified section references AND banned Act names.
    Replaces any unverified section or banned Act with '[unverified reference removed]' and logs it.
    """
    if not text or not isinstance(text, str):
        return text

    # Step 1: Sanitize banned Act names
    text = sanitize_banned_acts(text)

    # Step 2: Sanitize unverified section references
    unverified = scan_unverified_sections(text)
    if not unverified:
        return text

    # Log the event
    print(f"[SECURITY GUARD] Logged unverified section reference(s): {unverified}")

    sanitized = text
    for ref in set(unverified):
        pattern = re.compile(re.escape(ref), re.IGNORECASE)
        sanitized = pattern.sub("[unverified reference removed]", sanitized)

    return sanitized

