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
            "with the lessee that, if the latter pays the rent reserved by the lease and performs lease contracts, he may hold the property during the lease term without interruption.\n"
            "5. Plain Note on Scope: This section covers the tenant's duty to restore the property. It does not itself set rules for refunding deposits; deposit recovery usually rests on the rental agreement and a civil suit."
        ),
        "remedy_steps": [
            "Serve a 15-day formal Legal Demand Notice (established pre-litigation practice) citing Section 108(B)(m) demanding full refund of unlawfully deducted deposit amounts.",
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
            "Serve a 15-day formal Legal Demand Notice (established pre-litigation practice) to the seller and e-commerce platform.",
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
        "act": "General Legal Principle (Civil vs. Criminal Boundary - General Guidance)",
        "source_url": "https://nalsa.gov.in/",
        "verified_on": "2026-11-07",
        "status": "general_guidance",
        "sections": [],
        "key_provisions": (
            "1. General Guidance (Carries No Section Number): Mere failure to refund a deposit, pay wages, or fulfill a contract "
            "is fundamentally a civil dispute / breach of contract, not criminal cheating.\n"
            "2. Requirement for Criminal Offense: A criminal charge requires proof of dishonest or fraudulent intention at the very inception of the transaction.\n"
            "3. Caution on Police Complaints: Initiating criminal police complaints or FIRs for purely civil monetary disputes is legally improper and liable to rejection."
        ),
        "remedy_steps": [
            "Pursue civil remedies and statutory dispute forums (Rent Authority, Consumer Commission, Labor Authority).",
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

def retrieve_verified_legal_context(query: str, domain_filter: str = None, fallback_category: str = None) -> Dict[str, Any]:
    """
    Deterministically retrieves verified statutory provisions.
    Uses whole-word matching and excludes generic terms.
    If overriding out-of-scope topics match, REFUSES even if a civil domain also matched.
    If no domain matches and a fallback_category is provided (from dossier), reuses that category.
    If no domain matches and no fallback, returns an explicit out-of-scope fallback (no guessing).
    """
    query_str = str(query or "")

    # Overriding out-of-scope check: REFUSE even if a civil domain also matched
    for topic in OVERRIDING_OUT_OF_SCOPE_TOPICS:
        if _matches_word_beginning(topic, query_str):
            return {
                "matched_count": 0,
                "entries": [],
                "out_of_scope": True,
                "truly_out_of_scope": True,
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
    
    # If no domain keywords in follow-up message, reuse active case category from session dossier
    if not (is_tenancy or is_consumer or is_employment) and fallback_category:
        norm_cat = str(fallback_category).lower()
        if "tenant" in norm_cat or "rent" in norm_cat:
            is_tenancy = True
        elif "consumer" in norm_cat:
            is_consumer = True
        elif "employ" in norm_cat or "wage" in norm_cat or "salary" in norm_cat or "labor" in norm_cat:
            is_employment = True

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
            "truly_out_of_scope": True,
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
    """Normalizes section strings (e.g. 'Section 17(2)' -> '17(2)', '**Section 17 (2)**' -> '17(2)')."""
    s = s.strip().lower()
    s = re.sub(r'^(?:\*{0,2})(?:section|sec\.?|u/s)(?:\*{0,2})\s*', '', s)
    s = re.sub(r'[\s\u00a0\u202f\*]', '', s)
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

# Robust section scanner: handles bold markers, non-breaking spaces (\u00a0, \u202f), and clause spacing
SECTION_PATTERN = re.compile(
    r'(?i)\b\*{0,2}(?:section|sec\.?|u/s)\*{0,2}[\s\u00a0\u202f]*\*{0,2}([0-9]+(?:[\s\u00a0\u202f]*[\(\[][a-zA-Z0-9]+[\)\]])*(?:[a-zA-Z])*)'
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
        raw = match.group(0).strip()
        norm = normalize_section_reference(match.group(1))
        if norm in allowed:
            continue
        parent_clause = re.sub(r'\([a-zA-Z0-9]+\)$', '', norm)
        if parent_clause and parent_clause in allowed:
            continue
        base_num = re.match(r'^([0-9]+)', norm)
        if base_num and base_num.group(1) in allowed:
            continue
        unverified.append(raw)
    return unverified

# ==================== CASE-NAME GUARDRAIL ====================

# Each word in a party name begins with a capital letter (e.g. Ramesh, State, D.K., Ltd.)
_CAP_WORD = r"(?:(?:[A-Z]\.)+[A-Za-z0-9&']*(?:\.[A-Za-z0-9&']+)*|[A-Z][A-Za-z0-9&']*\.?)"
_JOINER = r"(?:of|and|the|for|in|&|de)"
_PARTY = rf"(?:{_CAP_WORD}(?:\s+(?:{_JOINER}\s+)?{_CAP_WORD}){{0,4}})"
_VS = r"(?:v\.|v|vs\.?|versus)"

CASE_NAME_PATTERN_STRICT = re.compile(rf"\b({_PARTY}\s+(?i:{_VS})\s+{_PARTY})\b")
_PREP_PREFIX = re.compile(r"^(?:in|under|see|also|refer to|citing|as per|as held in)\s+", re.IGNORECASE)

# Reporter citation patterns: e.g. (2000) 4 SCC 68, AIR 1985 SC 123, 1998 SCR 450, 2021 DHC 104
REPORTER_PATTERNS = [
    r'\b(?:\(\d{4}\)|\d{4})?\s*\d*\s*(?:SCC|AIR|SCR|DHC)(?:\s+(?:SC|Del|Bom|Cal|Kar|Mad|All|Online))?\s*\d+\b',
    r'\bAIR\s+\d{4}\s+(?:SC|[A-Z][a-z]+)\s+\d+\b',
    r'\(\d{4}\)\s*\d+\s+SCC\s+\d+\b'
]

# Judicial holdings phrases: e.g. "the Supreme Court held", "the High Court held", "courts have held/upheld"
JUDICIAL_HOLDING_PATTERNS = [
    r'(?i)[^.\n;!?]*(?:the\s+)?(?:Supreme\s+Court|High\s+Court|courts?)\s+(?:has\s+|have\s+)?(?:held|upheld)[^.\n;!?]*[.\n;!?]?',
]

# User requests for court case citations / precedents
CASE_LAW_REQUEST_PATTERNS = [
    r"\bcourt\s+cases?\b",
    r"\bcase\s+laws?\b",
    r"\bwhich\s+(?:court\s+)?case\b",
    r"\bcite\s+(?:a\s+)?(?:court\s+)?case\b",
    r"\bcite\s+(?:a\s+)?judgment\b",
    r"\bjudgm?ents?\b",
    r"\bprecedents?\b",
    r"\bSupreme\s+Court\s+says\b",
    r"\bHigh\s+Court\s+says\b",
    r"\bSupreme\s+Court\s+held\b",
    r"\bHigh\s+Court\s+held\b",
    r"\bcourt\s+held\b",
    r"\bcourts\s+have\s+held\b",
    r"\bcourt\s+order\b",
]

CASE_LAW_FIXED_REPLY = (
    "I can't cite court cases because I only use a small checked list of laws. "
    "A lawyer or the DLSA helpline 15100 can help with case law."
)

def is_case_law_request(text: str) -> bool:
    """Detects if user is asking for court cases, judgments, or judicial precedents."""
    if not text or not isinstance(text, str):
        return False
    for pat in CASE_LAW_REQUEST_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False

def scan_case_names(text: str) -> List[str]:
    """
    Scans text for adversarial or unverified judicial case citations
    such as 'X v. Y', 'X vs Y', 'X versus Y', reporter citations, or judicial holding sentences.
    Filters out non-case phrases like 'civil vs criminal'.
    """
    if not text or not isinstance(text, str):
        return []
    found = []
    # 1. Party vs Party matches
    for m in CASE_NAME_PATTERN_STRICT.finditer(text):
        matched_str = m.group(1).strip()
        cleaned = _PREP_PREFIX.sub("", matched_str).strip()
        cleaned = re.sub(r"[\.,;:!?]+$", "", cleaned).strip()
        
        # Check against exclusions like "civil vs criminal"
        norm_pair = re.sub(r"\s+", " ", cleaned.lower())
        norm_pair = re.sub(r"\.", "", norm_pair)
        if any(exc in norm_pair for exc in ["civil vs criminal", "criminal vs civil", "civil versus criminal", "criminal versus civil"]):
            continue
            
        if cleaned and cleaned not in found:
            found.append(cleaned)

    # 2. Reporter citations
    for pat in REPORTER_PATTERNS:
        for m in re.finditer(pat, text, re.IGNORECASE):
            rep = m.group(0).strip()
            if rep and rep not in found:
                found.append(rep)

    # 3. Judicial holding statements
    for pat in JUDICIAL_HOLDING_PATTERNS:
        for m in re.finditer(pat, text):
            holding = m.group(0).strip()
            if holding and holding not in found:
                found.append(holding)

    return found

def sanitize_case_names(text: str) -> str:
    """
    Replaces unverified case citations with '[unverified case reference removed]' and logs the event.
    """
    if not text or not isinstance(text, str):
        return text
    cases = scan_case_names(text)
    if not cases:
        return text
    print(f"[SECURITY GUARD] Logged unverified case reference(s): {cases}")
    sanitized = text
    for c in sorted(cases, key=len, reverse=True):
        pat = re.compile(re.escape(c), re.IGNORECASE)
        sanitized = pat.sub("[unverified case reference removed]", sanitized)
    return sanitized

def sanitize_unverified_sections(text: str) -> str:
    """
    Scans an AI answer for unverified section references, banned Act names, and unverified case citations.
    Replaces any unverified section or banned Act with '[unverified reference removed]',
    and any unverified case citation with '[unverified case reference removed]', and logs it.
    """
    if not text or not isinstance(text, str):
        return text

    # Step 1: Sanitize banned Act names
    text = sanitize_banned_acts(text)

    # Step 2: Sanitize unverified case citations
    text = sanitize_case_names(text)

    # Step 3: Sanitize unverified section references
    unverified = scan_unverified_sections(text)
    if not unverified:
        return text

    # Log the event
    print(f"[SECURITY GUARD] Logged unverified section reference(s): {unverified}")

    sanitized = text
    # Replace longer matches first with negative lookahead to prevent partial replacement of verified sections
    for ref in sorted(set(unverified), key=len, reverse=True):
        pattern = re.compile(rf"{re.escape(ref)}(?![0-9a-zA-Z\(\[])", re.IGNORECASE)
        sanitized = pattern.sub("[unverified reference removed]", sanitized)

    return sanitized

