using Microsoft.AspNetCore.Mvc;
using EmployeeManagement.Models;
using System.Collections.Generic;

namespace EmployeeManagement.Controllers
{
    public class ManagersController : Controller
    {
        public IActionResult Index()
        {
            // Sample data for demonstration
            var managers = new List<Manager>
            {
                new Manager { Id = 1, Name = "Alice Johnson", Position = "Manager", NumberOfTeams = 3 },
                new Manager { Id = 2, Name = "Bob Brown", Position = "Manager", NumberOfTeams = 5 }
            };

            return View(managers);
        }
    }
}
