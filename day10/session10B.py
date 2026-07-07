from session10 import FastTag,Vehicle
from session10A import TollPlazaQueue

def main():
    
    vehicle1 = Vehicle(
                        registration_no='PB10AL2937',
                        fasttag=FastTag(
                           fasttag_id=4019,
                           bank='SBI',
                           balance=500),
                        type='4W')
    vehicle2 = Vehicle(
                        registration_no='PB10GL5937',
                        fasttag=FastTag(
                           fasttag_id=4020,
                           bank='PNB',
                           balance=5000),
                        type='2W')
    vehicle3 = Vehicle(
                        registration_no='PB10AB2337',
                        fasttag=FastTag(
                           fasttag_id=4021,
                           bank='ICICI',
                           balance=4500),
                        type='4W')
    vehicle4 = Vehicle(
                        registration_no='PB10GX3307',
                        fasttag=FastTag(
                           fasttag_id=4022,
                           bank='SBI',
                           balance=3000),
                        type='2W')
    vehicle5 = Vehicle(
                        registration_no='PB10JU4235',
                        fasttag=FastTag(
                           fasttag_id=4023,
                           bank='HDFC',
                           balance=50),
                        type='4W')
    
    
    queue = TollPlazaQueue()
    queue.add(vehicle1)
    queue.add(vehicle2)
    queue.add(vehicle3)
    queue.add(vehicle4)
    queue.add(vehicle5)
    
    queue.deduct_toll(vehicle1)
    queue.deduct_toll(vehicle2)
    queue.deduct_toll(vehicle3)
    queue.deduct_toll(vehicle4)
    queue.deduct_toll(vehicle5)
    
    
    # Assignment: write the logic if balance is low, highlight the vehicle and do not remove from queue
    
if __name__ == '__main__':
    main()