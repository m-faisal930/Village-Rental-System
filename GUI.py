import tkinter as tk
from tkinter import ttk
import mysql.connector

class VillageRentalsApp:
    def __init__(self, root):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="village_rentals"
        )
        self.mycursor = self.mydb.cursor()

        self.root = root
        self.root.title("Village Rentals System")

        # Add a title label
        self.title_label = tk.Label(self.root, text="Village Rentals System", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        self.tabControl = ttk.Notebook(self.root)

        # Add Equipment Tab
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Add Equipment')
        self.tabControl.pack(expand=1, fill="both")
        self.add_equipment_label = tk.Label(self.tab1, text="Add Equipment")
        self.add_equipment_label.pack()

        self.name_label = tk.Label(self.tab1, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.tab1)
        self.name_entry.pack()

        self.description_label = tk.Label(self.tab1, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.tab1)
        self.description_entry.pack()

        self.category_label = tk.Label(self.tab1, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(self.tab1)
        self.category_entry.pack()

        self.daily_rental_cost_label = tk.Label(self.tab1, text="Daily Rental Cost:")
        self.daily_rental_cost_label.pack()
        self.daily_rental_cost_entry = tk.Entry(self.tab1)
        self.daily_rental_cost_entry.pack()

        self.add_equipment_button = tk.Button(self.tab1, text="Add Equipment", command=self.add_equipment)
        self.add_equipment_button.pack()

        # Add Client Tab
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='Add Client')
        self.tabControl.pack(expand=1, fill="both")

        self.add_client_label = tk.Label(self.tab2, text="Add Client")
        self.add_client_label.pack()

        self.last_name_label = tk.Label(self.tab2, text="Last Name:")
        self.last_name_label.pack()
        self.last_name_entry = tk.Entry(self.tab2)
        self.last_name_entry.pack()

        self.first_name_label = tk.Label(self.tab2, text="First Name:")
        self.first_name_label.pack()
        self.first_name_entry = tk.Entry(self.tab2)
        self.first_name_entry.pack()

        self.contact_phone_label = tk.Label(self.tab2, text="Contact Phone:")
        self.contact_phone_label.pack()
        self.contact_phone_entry = tk.Entry(self.tab2)
        self.contact_phone_entry.pack()

        self.email_label = tk.Label(self.tab2, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.tab2)
        self.email_entry.pack()

        self.add_client_button = tk.Button(self.tab2, text="Add Client", command=self.add_client)
        self.add_client_button.pack()

        # Delete Equipment Tab
        self.tab6 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab6, text='Delete Equipment')
        self.tabControl.pack(expand=1, fill="both")
        self.delete_equipment_label = tk.Label(self.tab6, text="Delete Equipment")
        self.delete_equipment_label.pack()





        self.equipment_id_label = tk.Label(self.tab6, text="Equipment ID:")
        self.equipment_id_label.pack()
        self.equipment_id_entry_to_delete = tk.Entry(self.tab6)
        self.equipment_id_entry_to_delete.pack()


        self.delete_equipment_button = tk.Button(self.tab6, text="Delete Equipment", command=self.delete_equipment)
        self.delete_equipment_button.pack()

        # Display Equipment Tab
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='Display Equipment')
        self.tabControl.pack(expand=1, fill="both")

        self.display_equipment_label = tk.Label(self.tab3, text="Display Equipment")
        self.display_equipment_label.pack()

        self.display_equipment_text = tk.Text(self.tab3)
        self.display_equipment_text.pack()

        self.display_equipment_button = tk.Button(self.tab3, text="Display Equipment", command=self.display_all_equipment)
        self.display_equipment_button.pack()

        # Display Clients Tab
        self.tab4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab4, text='Display Clients')
        self.tabControl.pack(expand=1, fill="both")
        self.display_clients_label = tk.Label(self.tab4, text="Display Clients")
        self.display_clients_label.pack()

        self.display_clients_text = tk.Text(self.tab4)
        self.display_clients_text.pack()

        self.display_clients_button = tk.Button(self.tab4, text="Display Clients", command=self.display_all_clients)
        self.display_clients_button.pack()

        # Process Rental Tab
        self.tab5 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab5, text='Process Rental')
        self.tabControl.pack(expand=1, fill="both")
        self.process_rental_label = tk.Label(self.tab5, text="Process Rental")
        self.process_rental_label.pack()

        self.client_id_label = tk.Label(self.tab5, text="Client ID:")
        self.client_id_label.pack()
        self.client_id_entry = tk.Entry(self.tab5)
        self.client_id_entry.pack()

        self.equipment_id_label = tk.Label(self.tab5, text="Equipment ID:")
        self.equipment_id_label.pack()
        self.equipment_id_entry = tk.Entry(self.tab5)
        self.equipment_id_entry.pack()

        self.rental_date_label = tk.Label(self.tab5, text="Rental Date:")
        self.rental_date_label.pack()
        self.rental_date_entry = tk.Entry(self.tab5)
        self.rental_date_entry.pack()

        self.return_date_label = tk.Label(self.tab5, text="Return Date:")
        self.return_date_label.pack()
        self.return_date_entry = tk.Entry(self.tab5)
        self.return_date_entry.pack()

        self.cost_label = tk.Label(self.tab5, text="Cost:")
        self.cost_label.pack()
        self.cost_entry = tk.Entry(self.tab5)
        self.cost_entry.pack()

        self.process_rental_button = tk.Button(self.tab5, text="Process Rental", command=self.process_rental)
        self.process_rental_button.pack()

        # Add padding to each tab for better spacing
        for tab in self.tabControl.tabs():
            self.tabControl.tab(tab, padding=(20, 5))

        # Call methods to create UI elements in each tab
        self.create_add_equipment_tab()
        self.create_add_client_tab()
        self.create_delete_equipment_tab()
        self.create_display_equipment_tab()
        self.create_display_clients_tab()
        self.create_process_rental_tab()

    def create_add_equipment_tab(self):
        self.add_equipment_label = tk.Label(self.tab1, text="Add Equipment", font=("Helvetica", 14, "bold"))
        self.add_equipment_label.pack()

        # Rest of the UI elements for adding equipment

    def create_add_client_tab(self):
        self.add_client_label = tk.Label(self.tab2, text="Add Client", font=("Helvetica", 14, "bold"))
        self.add_client_label.pack()

        # Rest of the UI elements for adding clients

    def create_delete_equipment_tab(self):
        self.delete_equipment_label = tk.Label(self.tab6, text="Delete Equipment", font=("Helvetica", 14, "bold"))
        self.delete_equipment_label.pack()

        # Rest of the UI elements for deleting equipment

    def create_display_equipment_tab(self):
        self.display_equipment_label = tk.Label(self.tab3, text="Display Equipment", font=("Helvetica", 14, "bold"))
        self.display_equipment_label.pack()

        # Rest of the UI elements for displaying equipment

    def create_display_clients_tab(self):
        self.display_clients_label = tk.Label(self.tab4, text="Display Clients", font=("Helvetica", 14, "bold"))
        self.display_clients_label.pack()

        # Rest of the UI elements for displaying clients

    def create_process_rental_tab(self):
        self.process_rental_label = tk.Label(self.tab5, text="Process Rental", font=("Helvetica", 14, "bold"))
        self.process_rental_label.pack()

        # Rest of the UI elements for processing rental
    def add_equipment(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        daily_rental_cost = float(self.daily_rental_cost_entry.get())
        sql = "INSERT INTO equipment (name, description, category, daily_rental_cost) VALUES (%s, %s, %s, %s)"
        val = (name, description, category, daily_rental_cost)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        self.name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.daily_rental_cost_entry.delete(0, tk.END)

    def delete_equipment(self):
        equipment_id = self.equipment_id_entry_to_delete.get() # Retrieve equipment ID when the button is clicked
        try:
            equipment_id = int(equipment_id) # Convert to int if needed

            # Delete related rentals first
            sql_rentals = "DELETE FROM rentals WHERE equipment_id = %s"
            self.mycursor.execute(sql_rentals, (equipment_id,))
            self.mydb.commit()

            # Then delete the equipment
            sql_equipment = "DELETE FROM equipment WHERE id = %s"
            self.mycursor.execute(sql_equipment, (equipment_id,))
            self.mydb.commit()

            self.equipment_id_entry_to_delete.delete(0, tk.END)
        except ValueError:
            print("Please enter a valid equipment ID.")

    def add_client(self):
        last_name = self.last_name_entry.get()
        first_name = self.first_name_entry.get()
        contact_phone = self.contact_phone_entry.get()
        email = self.email_entry.get()
        sql = "INSERT INTO clients (last_name, first_name, contact_phone, email) VALUES (%s, %s, %s, %s)"
        val = (last_name, first_name, contact_phone, email)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        self.last_name_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.contact_phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def display_all_equipment(self):
        self.display_equipment_text.delete(1.0, tk.END)
        self.mycursor.execute("SELECT * FROM equipment")
        equipment_data = self.mycursor.fetchall()
        for equipment in equipment_data:
            self.display_equipment_text.insert(tk.END, f"{equipment}\n")

    def display_all_clients(self):
        self.display_clients_text.delete(1.0, tk.END)
        self.mycursor.execute("SELECT * FROM clients")
        clients_data = self.mycursor.fetchall()
        for client in clients_data:
            self.display_clients_text.insert(tk.END, f"{client}\n")

    def process_rental(self):
        client_id = int(self.client_id_entry.get())
        equipment_id = int(self.equipment_id_entry.get())
        print("equipment id is: ",equipment_id)
        rental_date = self.rental_date_entry.get()  # Format: YYYY-MM-DD
        return_date = self.return_date_entry.get()  # Format: YYYY-MM-DD
        cost = float(self.cost_entry.get())
        sql = "INSERT INTO rentals (client_id, equipment_id, rental_date, return_date, cost) VALUES (%s, %s, %s, %s, %s)"
        val = (client_id, equipment_id, rental_date, return_date, cost)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        self.client_id_entry.delete(0, tk.END)
        self.equipment_id_entry.delete(0, tk.END)
        self.rental_date_entry.delete(0, tk.END)
        self.return_date_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VillageRentalsApp(root)
    root.mainloop()
