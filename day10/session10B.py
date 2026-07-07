from session10 import FastTag, Vehicle
from session10A import TollPlazaQueue


def main():

    vehicle1 = Vehicle(
        registration_no='PB10AL2937',
        fasttag=FastTag(4019, 'SBI', 500),
        type='4W'
    )

    vehicle2 = Vehicle(
        registration_no='PB10GL5937',
        fasttag=FastTag(4020, 'PNB', 5000),
        type='2W'
    )

    vehicle3 = Vehicle(
        registration_no='PB10AB2337',
        fasttag=FastTag(4021, 'ICICI', 4500),
        type='4W'
    )

    vehicle4 = Vehicle(
        registration_no='PB10GX3307',
        fasttag=FastTag(4022, 'SBI', 3000),
        type='2W'
    )

    vehicle5 = Vehicle(
        registration_no='PB10JU4235',
        fasttag=FastTag(4023, 'HDFC', 50),
        type='4W'
    )

    queue = TollPlazaQueue()

    queue.add(vehicle1)
    queue.add(vehicle2)
    queue.add(vehicle3)
    queue.add(vehicle4)
    queue.add(vehicle5)

    print("\n========== Processing Queue ==========\n")

    while queue.size > 0:

        queue.deduct_toll()

        # Stop if first vehicle has insufficient balance
        if queue.head is not None:
            toll = 100 if queue.head.type == '4W' else 50

            if queue.head.fasttag.balance < toll:
                break

    print("\n========== Remaining Queue ==========\n")

    queue.show_list()

    print(f"\nRemaining Vehicles : {queue.size}")


if __name__ == "__main__":
    main()