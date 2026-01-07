def calculate_base_fee(student_class: int) -> int:
    """
    Calculate base fee based on class rules.
    Class 1–5  : +1000 per class
    Class 6–10 : +1500 per class (after class 5)
    """

    if student_class <= 5:
        return student_class * 1000
    else:
        return 5000 + (student_class - 5) * 1500

def calculate_final_fee(
    student_class: int,
    carried_forward: int = 0,
    override_fee: int | None = None,
    paid_amount: int = 0
) -> dict:
    """
    Calculate final fee details for a student.
    """

    base_fee = calculate_base_fee(student_class)

    final_fee = override_fee if override_fee is not None else base_fee

    total_due = final_fee + carried_forward

    balance = total_due - paid_amount

    if balance <= 0:
        status = "paid"
        balance = 0
    elif paid_amount > 0:
        status = "partial"
    else:
        status = "pending"

    return {
        "base_fee": base_fee,
        "final_fee": final_fee,
        "carried_forward": carried_forward,
        "total_due": total_due,
        "paid_amount": paid_amount,
        "balance": balance,
        "status": status
    }
