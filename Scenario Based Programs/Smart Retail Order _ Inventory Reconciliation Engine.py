"""Smart Retail Order & Inventory Reconciliation Engine

A regional e-commerce warehouse needs an automated reconciliation engine to process daily customer orders.
Product master data is stored using immutable tuples "(product_name, unit_price)", stock quantities are stored in a dictionary,
and raw order logs arrive as messy comma-separated strings.
To prevent fraudulent or accidental duplicate line items within a single order string, duplicate product codes in the same order
must be filtered out using a set before stock deduction.
Finally, all valid order totals must be stored in a memory-efficient floating-point "array" ("d") for end-of-day financial auditing.

Modular Design Requirements:
1. "parse_order_line(raw_line)": Cleans the string, extracts the "order_id", and returns a tuple "(order_id, unique_product_codes_set)".
2. "process_order(order_id, product_codes, *, catalog, stock, tax_rate=0.18)": Uses keyword-only arguments for "catalog" and "stock".
    Checks if requested items are in "stock" (quantity > 0).
    Deducts 1 unit per available product, calculates the taxed total, and returns "(billed_amount, out_of_stock_list)".
3. "reconcile_daily_batch(raw_orders, catalog, stock, tax_rate=0.18)": Orchestrates the batch processing,
    stores non-zero billed amounts in an "array.array("d")", and prints the summary report.

Input Description
- "catalog": Dictionary mapping "product_code" to "(product_name, unit_price)" tuple.
- "stock": Dictionary mapping "product_code" to integer available quantity.
- "raw_orders": List of raw order strings formatted as "ORDER_ID | code1, code2, code3...".

Output Description
- For each order, print: "Order <ORDER_ID>: Billed Rs.<Amount> | Out of Stock: <Sorted_List_of_Unavailable_Codes>"
  (Amount formatted to 2 decimal places).
- On the second-to-last line, print: "Remaining Stock: <stock_dict_sorted_by_key>"
- On the last line, print: "Audit Array: <list_of_billed_floats> | Grand Total: Rs.<Total>

This code also contains 2 test cases that need to be executed seperately"""

import array


def parse_order_line(raw_line):
    raw_line_split = raw_line.split("|")
    order_id, raw_item_list = raw_line_split[0].strip(), raw_line_split[1].split(",")
    unique_item_list = {item.strip() for item in raw_item_list}
    return order_id, unique_item_list


def process_order(order_id, product_codes, *, catalog, stock, tax_rate=0.18):
    bill_amt = 0
    out_of_stock = []
    for item_code in product_codes:
        if stock.get(item_code, 0) > 0:
            bill_amt += round(catalog[item_code][1], 2)
            stock[item_code] -= 1
        else:
            out_of_stock.append(item_code)
        final_amt = round(bill_amt * (1 + tax_rate), 2)
    return final_amt, out_of_stock


def reconcile_daily_batch(raw_orders, catalog, stock, tax_rate=0.18):
    audit_array = array.array("d", [])
    for order in raw_orders:
        order_id, item_list = parse_order_line(order)
        bill_amt, out_of_stock = process_order(
            order_id, item_list, catalog=catalog, stock=stock, tax_rate=tax_rate
        )
        if bill_amt > 0:
            audit_array.append(bill_amt)
        print(
            f"Order {order_id}: Billed Rs.{bill_amt:.2f} | Out of Stock: {sorted(out_of_stock)}"
        )
    sorted_stock = {k: stock[k] for k in sorted(stock)}
    print(f"Remaining Stock: {sorted_stock}")
    print(
        f"Audit Array: {audit_array.tolist()} | Grand Total: Rs.{sum(audit_array):.2f}"
    )


"""# --- Problem 1: Test Case 1 ---
import io
from contextlib import redirect_stdout

catalog_tc1 = {
    "P101": ("Wireless Mouse", 500.0),
    "P102": ("Mechanical Keyboard", 1500.0),
    "P103": ("USB-C Hub", 800.0),
    "P104": ("Laptop Stand", 1000.0),
}
stock_tc1 = {"P101": 2, "P102": 1, "P103": 0, "P104": 3}
orders_tc1 = ["ORD-01 | P101, P102, P101, P103", "ORD-02 | P102, P104", "ORD-03 | P103"]

assert parse_order_line("ORD-01 | P101, P102, P101") == (
    "ORD-01",
    {"P101", "P102"},
), "parse_order_line failed"

buf = io.StringIO()
with redirect_stdout(buf):
    reconcile_daily_batch(orders_tc1, catalog_tc1, stock_tc1)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "Order ORD-01: Billed Rs.2360.00 | Out of Stock: ['P103']\n"
    "Order ORD-02: Billed Rs.1180.00 | Out of Stock: ['P102']\n"
    "Order ORD-03: Billed Rs.0.00 | Out of Stock: ['P103']\n"
    "Remaining Stock: {'P101': 1, 'P102': 0, 'P103': 0, 'P104': 2}\n"
    "Audit Array: [2360.0, 1180.0] | Grand Total: Rs.3540.00"
)
assert (
    actual_out == expected_out
), f"Test Case 1 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 1 - Test Case 1 Passed!")"""


"""# --- Problem 1: Test Case 2 ---
catalog_tc2 = {"A1": ("SSD 1TB", 4000.0), "A2": ("RAM 16GB", 3000.0)}
stock_tc2 = {"A1": 1, "A2": 2}
orders_tc2 = ["ORD-101 | A1, A1, A1, A2", "ORD-102 | A1, A2"]

buf = io.StringIO()
with redirect_stdout(buf):
    reconcile_daily_batch(orders_tc2, catalog_tc2, stock_tc2, tax_rate=0.10)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "Order ORD-101: Billed Rs.7700.00 | Out of Stock: []\n"
    "Order ORD-102: Billed Rs.3300.00 | Out of Stock: ['A1']\n"
    "Remaining Stock: {'A1': 0, 'A2': 0}\n"
    "Audit Array: [7700.0, 3300.0] | Grand Total: Rs.11000.00"
)
assert (
    actual_out == expected_out
), f"Test Case 2 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 1 - Test Case 2 Passed!")"""
