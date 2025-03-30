using Microsoft.AspNetCore.Mvc;

namespace EmployeeManagement.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            // Redirects to the Index action of the EmployeesController
            return RedirectToAction("Index", "Employees");
        }
    }
}
