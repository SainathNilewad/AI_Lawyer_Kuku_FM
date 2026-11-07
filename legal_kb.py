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
        "source_url": "https://www.indiacode.nic.in/",
        "verified_on": "<to be filled after check>",
        "status": "needs_my_verification",
        "sections": ["Section 13", "Section 14", "Section 21"],
        "key_provisions": (
            "1. Note on Enforceability: The Model Tenancy Act, 2021 is a model law drafted by the Central Government "
            "and binds only States and Union Territories that have formally adopted or enacted it. State rent laws vary.\n"
            "2. Security Deposit Cap: Security deposit for residential premises cannot exceed 2 months' rent.\n"
            "3. Refund Timeline: Landlord must refund the security deposit within 30 days of the tenant handing over peaceful possession, "
            "after deducting agreed legitimate dues.\n"
            "4. Normal Wear and Tear: Landlords cannot deduct deposit for ordinary wear-and-tear (e.g., natural fading of wall paint, "
            "minor aging of fixtures). Deductions must be substantiated with itemized bills.\n"
            "5. Rent Authority: Disputes over deposit withholding or eviction must be filed before the Rent Authority/Rent Court, "
            "not a regular civil court."
        ),
        "remedy_steps": [
            "Send formal written demand notice giving 15 days to refund deposit with interest for delay.",
            "If unresponsive, register grievance on the State Rent Authority Portal or National Consumer Helpline.",
            "File petition before local Rent Authority / Small Causes Court for refund with interest and damages (subject to state adoption)."
        ]
    },
    {
        "domain": "Tenancy & Rental",
        "act": "Transfer of Property Act, 1882",
        "source_url": "https://www.indiacode.nic.in/",
        "verified_on": "<to be filled after check>",
        "status": "needs_my_verification",
        "sections": ["Section 108(B)(m)", "Section 108(B)(q)"],
        "key_provisions": (
            "Tenant is bound to keep the property in as good condition as it was when put into possession, "
            "'subject only to the changes caused by reasonable wear and tear or irresistible force'. "
            "Tenant has right to receive back deposit upon vacating and handing over vacant possession."
        ),
        "remedy_steps": ["Issue formal Legal Notice through registered post or legal email before litigation."]
    },

    # ==================== CONSUMER & E-COMMERCE DISPUTES ====================
    {
        "domain": "Consumer Protection",
        "act": "Consumer Protection Act, 2019 (CPA 2019)",
        "source_url": "https://www.indiacode.nic.in/",
        "verified_on": "<to be filled after check>",
        "status": "needs_my_verification",
        "sections": ["Section 2(7)", "Section 2(11)", "Section 2(47)", "Section 35", "Section 84"],
        "key_provisions": (
            "1. Consumer Definition (Sec 2(7)): Any person who buys goods or hires services for consideration, including online/offline.\n"
            "2. Deficiency in Service (Sec 2(11)): Any fault, imperfection, shortcoming or inadequacy in quality, nature, and manner of performance.\n"
            "3. Unfair Trade Practice (Sec 2(47)): False representation of goods, refusal to issue refunds for defective items within reasonable time, "
            "or one-sided terms.\n"
            "4. Product Liability (Sec 84): Manufacturer or seller is liable to compensate consumer for harm caused by defective product.\n"
            "5. Jurisdiction & Filing (Sec 35): Filing of complaint before the District Consumer Commission. (Exact section for territorial and pecuniary jurisdiction to be confirmed from official text).\n"
            "6. Online Filing (e-Daakhil): Consumers can file complaints completely online via edaakhil.nic.in without hiring a lawyer."
        ),
        "remedy_steps": [
            "Lodge formal complaint on National Consumer Helpline (NCH) toll-free 1915 or consumerhelpline.gov.in.",
            "Serve a 15-day formal Legal Notice to the seller and e-commerce marketplace.",
            "File consumer complaint online on e-Daakhil portal (edaakhil.nic.in) with order invoice, defect photos, and communication proof."
        ]
    },

    # ==================== EMPLOYMENT & SALARY DISPUTES ====================
    {
        "domain": "Employment & Labor",
        "act": "Code on Wages, 2019",
        "source_url": "https://www.indiacode.nic.in/",
        "verified_on": "<to be filled after check>",
        "status": "needs_my_verification",
        "sections": ["Section 17(2)", "Section 17(4)", "Section 18(1)", "Section 18(3)"],
        "key_provisions": (
            "1. Payment of Wages on Removal, Dismissal or Resignation (Section 17(2)): Wages of an employee who is removed, dismissed, "
            "retrenched or resigns must be paid within two working days of that event.\n"
            "2. Other Laws Preserved (Section 17(4)): The Code does not affect any time limit for payment of wages given in any other law (state rules may differ).\n"
            "3. Authorised Deductions Only (Section 18(1)): No deductions from wages except those authorised by the Code.\n"
            "4. Deduction Limits (Section 18(3)): Total deductions in a wage period are capped.\n"
            "5. Claims and Forum: Procedure and forum vary; confirm from the official text or ask a lawyer / DLSA 15100."
        ),
        "remedy_steps": [
            "Send formal written demand email to employer requesting immediate release of unpaid wages and dues.",
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

# Real Lawyer Escalation Rules (Whole-word matching)
CRITICAL_ESCALATION_CRITERIA = [
    "cognizable violent crime",
    "arrest",
    "bail",
    "domestic violence",
    "physical harm",
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
    "weapon"
]

# Domain keyword lists (strictly whole-word matched, generic words removed)
TENANCY_KEYWORDS = ["rent", "rental", "landlord", "tenant", "deposit", "flat", "lease", "evict", "broker"]
CONSUMER_KEYWORDS = ["refund", "product", "defective", "flipkart", "amazon", "seller", "warranty", "ecommerce", "consumer", "service", "repair", "replacement", "replace"]
EMPLOYMENT_KEYWORDS = ["salary", "employer", "resignation", "relieving", "wages", "terminated", "fnf", "dues"]

def _matches_any_whole_word(text: str, keywords: List[str]) -> bool:
    """Matches keywords as whole words only to prevent false substring triggers."""
    return any(re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE) for kw in keywords)

def retrieve_verified_legal_context(query: str, domain_filter: str = None) -> Dict[str, Any]:
    """
    Deterministically retrieves verified statutory provisions.
    Uses whole-word matching and excludes generic terms.
    If no domain matches, returns an explicit out-of-scope fallback (no guessing).
    """
    query_str = str(query or "")
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
    Matches whole words only to prevent false triggers (e.g. 'bail' inside other words).
    """
    text_str = str(text or "")
    escalation_reasons = []
    
    for trigger in CRITICAL_ESCALATION_CRITERIA:
        if re.search(r'\b' + re.escape(trigger) + r'\b', text_str, re.IGNORECASE):
            escalation_reasons.append(trigger)
            
    # Whole-word check for high-risk words
    for w in HIGH_RISK_WORDS:
        if re.search(r'\b' + re.escape(w) + r'\b', text_str, re.IGNORECASE):
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
    Collects every allowed section reference from the verified statutory database.
    Includes both full clauses ('17(2)', '108(b)(m)') and parent section numbers ('17', '108').
    """
    allowed: Set[str] = set()
    for entry in VERIFIED_STATUTORY_DATABASE:
        for s in entry.get("sections", []):
            norm = normalize_section_reference(s)
            if norm:
                allowed.add(norm)
                base = re.match(r'^([0-9]+)', norm)
                if base:
                    allowed.add(base.group(1))
    return allowed

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
    Scans an AI answer for section references. If an unknown section appears,
    adds a visible warning '[unverified reference removed]' and logs it.
    """
    if not text or not isinstance(text, str):
        return text

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

