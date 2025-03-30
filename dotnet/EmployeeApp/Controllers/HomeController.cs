using EmployeeApp.Models;
using EmployeeApp.Extensions;
using Microsoft.AspNetCore.Mvc;

namespace EmployeeApp.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            var employee = new Employee
            {
                FirstName = "John",
                LastName = "Doe",
                Email = "john.doe@example.com",
                Salary = 50000
            };

            var fullName = employee.GetFullName();

            ViewData["FullName"] = fullName;
            return View();
        }
    }
}
