using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Caching.Memory;  // Import necessary namespace

namespace CachingDemoApp.Controllers  // Ensure the correct namespace is used
{
    public class HomeController : Controller
    {
        private readonly IMemoryCache _memoryCache;

        // Inject IMemoryCache through the constructor
        public HomeController(IMemoryCache memoryCache)
        {
            _memoryCache = memoryCache;
        }

        // Apply Response Caching
        [ResponseCache(Duration = 60)]
        public IActionResult Index()
        {
            ViewBag.Timestamp = DateTime.Now;

            // Implement Data Caching using IMemoryCache
            if (!_memoryCache.TryGetValue("CachedTime", out string cachedTime))
            {
                // Cache the current time if not already cached
                cachedTime = DateTime.Now.ToString("T");

                var cacheEntryOptions = new MemoryCacheEntryOptions()
                    .SetSlidingExpiration(TimeSpan.FromSeconds(30)) // Reset the expiration time if accessed within 30 seconds
                    .SetAbsoluteExpiration(TimeSpan.FromMinutes(1)); // Max cache time is 1 minute

                _memoryCache.Set("CachedTime", cachedTime, cacheEntryOptions);
            }

            ViewBag.CachedTime = cachedTime;

            return View();
        }
    }
}
