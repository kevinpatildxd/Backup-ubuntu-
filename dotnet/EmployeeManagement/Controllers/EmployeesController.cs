using Microsoft.AspNetCore.Mvc;
using EmployeeManagement.Models;
using System.Collections.Generic;

namespace EmployeeManagement.Controllers
{
    public class EmployeesController : Controller
    {
        public IActionResult Index()
        {
            // Sample data for demonstration purposes
            var employees = new List<Employee>
            {
                new Employee { Id = 1, Name = "John Doe", Position = "Manager" },
                new Employee { Id = 2, Name = "Jane Smith", Position = "Clerk" }
            };

            // Pass the list of employees to the view
            return View(employees);
        }
    }
}
