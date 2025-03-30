using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System;

namespace CookieSessionDemo.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            // Set a cookie
            Response.Cookies.Append("UserName", "JohnDoe", new CookieOptions { Expires = DateTimeOffset.UtcNow.AddDays(1) });

            // Set session value
            HttpContext.Session.SetString("SessionKey", "SessionValue");

            return View();
        }

        public IActionResult About()
        {
            // Read cookie
            ViewBag.UserName = Request.Cookies["UserName"];

            // Read session value
            ViewBag.SessionValue = HttpContext.Session.GetString("SessionKey");

            return View();
        }

        public IActionResult QueryStringDemo(string name)
        {
            ViewBag.Name = name;
            return View();
        }

        [HttpPost]
        public IActionResult HiddenFieldDemo(string hiddenFieldValue)
        {
            ViewBag.HiddenFieldValue = hiddenFieldValue;
            return View();
        }
    }
}
