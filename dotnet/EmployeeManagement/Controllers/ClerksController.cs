using Microsoft.AspNetCore.Mvc;
using EmployeeManagement.Models;
using System.Collections.Generic;

namespace EmployeeManagement.Controllers
{
    public class ClerksController : Controller
    {
        public IActionResult Index()
        {
            // Sample data for demonstration
            var clerks = new List<Clerk>
            {
                new Clerk { Id = 1, Name = "Charlie Smith", Position = "Clerk", Department = "Finance" },
                new Clerk { Id = 2, Name = "Dana White", Position = "Clerk", Department = "HR" }
            };

            return View(clerks);
        }
    }
}
