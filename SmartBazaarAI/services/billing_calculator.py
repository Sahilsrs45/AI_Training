CATEGORY_DISCOUNT = {
    "Grocery": 5,
    "Household": 10,
    "Personal Care": 8
}


MEMBERSHIP_DISCOUNT = {
    "Regular": 0,
    "Silver": 2,
    "Gold": 5,
    "Platinum": 8
}


def calculate_invoice(request):

    subtotal = 0
    category_discount = 0

    item_details = []

    for item in request.items:

        line_total = (
            item.quantity *
            item.unit_price
        )

        discount_percent = CATEGORY_DISCOUNT[
            item.category
        ]

        discount_amount = (
            line_total *
            discount_percent
        ) / 100

        discounted_value = (
            line_total -
            discount_amount
        )

        subtotal += line_total

        category_discount += (
            discount_amount
        )

        item_details.append(
            {
                "name": item.name,
                "line_total": round(
                    line_total,
                    2
                ),
                "discounted_value":
                    round(
                        discounted_value,
                        2
                    ),
                "gst_rate":
                    item.gst_rate
            }
        )

    after_category_discount = (
        subtotal -
        category_discount
    )

    membership_discount = (
        after_category_discount *
        MEMBERSHIP_DISCOUNT[
            request.membership_tier
        ]
    ) / 100

    after_membership_discount = (
        after_category_discount -
        membership_discount
    )

    coupon_discount = 0

    if (
        request.coupon_code ==
        "SMART100"
        and
        after_membership_discount >= 2000
    ):
        coupon_discount = 100

    after_coupon = (
        after_membership_discount -
        coupon_discount
    )

    max_allowed_points = min(
        200,
        int(after_coupon * 0.10)
    )

    points_to_redeem = min(
        request.loyalty_points_to_redeem,
        request.loyalty_points_available,
        max_allowed_points
    )

    after_loyalty = (
        after_coupon -
        points_to_redeem
    )

    gst_total = 0

    for item in item_details:

        gst_amount = (
            item["discounted_value"]
            *
            item["gst_rate"]
        ) / 100

        gst_total += gst_amount

    final_amount = (
        after_loyalty +
        gst_total
    )

    earned_points = int(
        final_amount // 100
    )

    return {

        "customer_name":
            request.customer_name,

        "subtotal":
            round(subtotal, 2),

        "category_discount":
            round(
                category_discount,
                2
            ),

        "membership_discount":
            round(
                membership_discount,
                2
            ),

        "coupon_discount":
            round(
                coupon_discount,
                2
            ),

        "loyalty_redeemed":
            points_to_redeem,

        "gst":
            round(
                gst_total,
                2
            ),

        "final_amount":
            round(
                final_amount,
                2
            ),

        "remaining_points":
            request.loyalty_points_available -
            points_to_redeem,

        "earned_points":
            earned_points
    }