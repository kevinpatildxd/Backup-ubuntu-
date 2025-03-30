using System.Net.Http;
using System.Threading.Tasks;

namespace WebDownloader.Services
{
    public interface IWebDownloadService
    {
        Task<string> DownloadContentAsync(string url);
    }

    public class WebDownloadService : IWebDownloadService
    {
        private readonly HttpClient _httpClient;

        public WebDownloadService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<string> DownloadContentAsync(string url)
        {
            var response = await _httpClient.GetStringAsync(url);
            return response;
        }
    }
}
