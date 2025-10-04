from company import Company
from vehicle import Vehicle
from customer import Customer

def printMenu():
    print('\n######################')
    print('1: Add new vehicle.')
    print('2: Add new customer.') 
    print('3: Rent vehicle.') 
    print('4: Return rented vehicle.') 
    print('5: Print summary.') 
    print('6: Exit.') 
    print('######################\n')

def start():
    company = Company("Pythonic Car Rental Company")
    company.add_vehicle(Vehicle("Nissan", 10.0, "7bc123"))
    company.add_vehicle(Vehicle("Toyota", 20.0, "7ts123"))
    company.add_vehicle(Vehicle("Tesla", 40.0, "7t0333"))
    company.add_customer(Customer("Andleeb", "1234567890"))
    company.add_customer(Customer("Andrew Sagan", "1666567890"))
    company.add_customer(Customer("John Carl", "1666567890"))
    
    while True:
        printMenu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            try:
                model = input("Vehicle Model: ")
                rental_rate = float(input("Rental rate: "))
                vin = input("VIN: ")
                vehicle_object = Vehicle(model, rental_rate, vin)
                company.add_vehicle(vehicle_object)
                print("Vehicle added successfully!")
            except ValueError:
                print("ValueError")

        elif choice == '2':
            name = input("Customer name: ")
            phone_number = input("Phone number: ")
            if len(phone_number) != 10 or not phone_number.isdigit():
                print("Invalid phone number. Phone number must be 10 digits.")
            else:
                theCustomer = Customer(name, phone_number)
                if company.add_customer(theCustomer):
                    print("Customer added successfully.")
                else:
                    print("Customer already exists.")

        elif choice == '3':
            customer_name = input("customer name: ")
            vin = input("VIN: ")
            rental_duration = int(input("Days of Rental: "))
            if company.rent_vehicle(customer_name, vin, rental_duration):
                print("Vehicle rented successfully.")
            else:
                print("Failed to rent the vehicle.")

        elif choice == '4':
            customer_name = input("Customer name: ")
            vin = input("VIN: ")
            customer = None
            for c in company.get_customers():
                if c.get_name() == customer_name:
                    customer = c
                    break
            if customer is not None:
                if customer.return_rented_vehicle(vin):
                    print("Vehicle returned successfully.")
                else:
                    print("Failed to return the vehicle.")
            else:
                print("Customer not found.")

        elif choice == '5':
            file_name = input("Enter file name: ")
            if not file_name.endswith('.txt'):
                file_name += '.txt'
            company.get_summary(file_name)
            
        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    start()
    

