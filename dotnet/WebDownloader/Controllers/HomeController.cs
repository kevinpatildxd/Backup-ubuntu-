using Microsoft.AspNetCore.Mvc;
using WebDownloader.Services;
using System.Threading.Tasks;

namespace WebDownloader.Controllers
{
    public class HomeController : Controller
    {
        private readonly IWebDownloadService _webDownloadService;

        public HomeController(IWebDownloadService webDownloadService)
        {
            _webDownloadService = webDownloadService;
        }

        public async Task<IActionResult> Index(string url)
        {
            if (string.IsNullOrEmpty(url))
            {
                return View("Index", null);
            }

            var content = await _webDownloadService.DownloadContentAsync(url);
            ViewBag.Content = content;
            return View();
        }
    }
}
