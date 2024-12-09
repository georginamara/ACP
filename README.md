# eBarangay Certificates System  

## Description  
The **eBarangay Certificates System** is a Python-based application that digitizes the management of barangay certificates and citizen records. It streamlines processes such as adding, updating, searching, and deleting records, significantly improving efficiency and transparency in barangay services. This system is designed to address the inefficiencies of manual record-keeping by offering a modern, user-friendly digital solution.


## Project Overview  
The **eBarangay Certificates System** aims to simplify the management of barangay certificates by automating the process of storing, retrieving, and updating citizen records.  

### **Key Features**  
1. **User Authentication**: A login system ensures secure access to the application.  
2. **CRUD Operations**: Users can add, update, delete, and search citizen records.  
3. **Search and Filter**: Users can search for records using criteria like name, OR number, or certificate type.  
4. **Tabular Data Display**: Records are displayed in a scrollable table for easy navigation and organization.  

By automating these tasks, the system improves processing time by up to 60% and ensures accuracy and accessibility in record management. The primary users are barangay officials responsible for managing citizen records and issuing certificates.


## Python Concepts, Libraries, and Techniques Applied  
This project incorporates several Python concepts and libraries:  

1. **Tkinter for GUI Development**:  
   - Used to create a user-friendly interface for forms, tables, and input fields.  
   - The `Label`, `Entry`, and `Button` widgets enable data input and interaction, while the `Treeview` widget provides a structured table view for records.

2. **pymysql for Database Management**:  
   - Handles database connections and CRUD operations.  
   - Ensures secure storage of citizen records in a MySQL database using parameterized queries to prevent SQL injection.

3. **StringVar for Variable Binding**:  
   - Binds GUI components (e.g., input fields) to Python variables, enabling seamless data exchange between the interface and backend logic.

4. **Exception Handling**:  
   - Ensures the system is robust by catching and handling errors, such as database connection issues or invalid user inputs, to prevent application crashes.

5. **Search Functionality**:  
   - Dynamically filters records based on user-defined criteria using SQL queries, with results displayed in real-time in the GUI.


## Integration with Sustainable Development Goals (SDGs)  

The **eBarangay Certificates System** contributes to two key Sustainable Development Goals:  

1. **SDG 11: Sustainable Cities and Communities**  
   - The system reduces manual paperwork and improves access to essential services, making barangay governance more efficient and sustainable.  

2. **SDG 16: Peace, Justice, and Strong Institutions**  
   - By ensuring accuracy and transparency in citizen records, the system fosters accountability and trust in local governance.  

Through its digitization efforts, the project modernizes barangay operations while promoting sustainable and transparent governance.


## Instructions for Running the Program  
I. Login to Access the System
- Upon running the program, a login screen will appear.
- Enter the default admin credentials:
  - Username: admin
  - Password: 1234
- If the credentials are correct, the main system interface will open. If incorrect, an error message will appear, and you can try again.

II. Add a New Citizen Record
- On the left side of the window, enter the following details:
  - OR Number
  - Name
  - Sitio
  - Age
  - Birthdate
  - Date Issued
  - Certificate Type
  - Amount
- Once the information is entered, click the "Save" button to store the record.
- The new record will automatically appear in the table of citizen records.

III. Update a Record
- Select the record you wish to update from the table by clicking on it.
- The system will populate the input fields with the selected record's details.
- Modify the necessary fields (e.g., Name, Sitio, or Certificate Type).
- Click the "Update" button to save the changes.
- The system will reflect the updated information in the table.

IV. Search for Records
- Use the Search bar to filter records.
- Select a search criterion from the dropdown menu (e.g., OR Number, Name, Certificate Type).
- Enter the search term in the input field and click the "Search" button.
- The system will display the records matching your criteria in the table.

V. Delete a Record
- Select the record you want to delete from the table by clicking on it.
- Click the "Delete" button.
- A confirmation dialog will appear to ensure you want to delete the record.
- Upon confirmation, the record will be removed from the table and the database.

VI. View All Records (Dashboard)
- The main table displays all stored citizen records, including:
  - OR Number
  - Name
  - Sitio
  - Age
  - Birthdate
  - Date Issued
  - Certificate Type
  - Amount
- Use the scrollbars to navigate through large datasets.
