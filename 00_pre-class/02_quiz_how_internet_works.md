## **Instructions**  
**Objective:** The goal of this exercise is to help you develop a foundational understanding of web navigation and its components, which are crucial for effective web scraping.

By the end of this exercise, you will have a strong foundational knowledge of how URLs, DNS, hyperlinks, and web servers work, and how this knowledge is applied in web scraping. 🚀  

---

## **Questions**  
1. **What are the main components of a URL, and what is the function of each component?**  

    . Identifikasi sumber daya di internet. Fungsi utama URL adalah untuk mengidentifikasi sumber daya yang ada di internet, seperti halaman web, dokumen, gambar, video, atau file lainnya. Dengan menggunakan URL, pengguna dapat menemukan dan mengakses sumber daya yang mereka butuhkan dengan mudah
    . Menghubungkan pengguna dengan server. URL memungkinkan browser pengguna untuk berkomunikasi dengan server yang menyimpan sumber daya tersebut. Browser akan mengirimkan request ke server berdasarkan URL yang diberikan, dan server akan merespon dengan menyediakan sumber daya yang diminta.
    . Menjaga struktur dan organisasi situs web. Dengan menggunakan URL, pemilik situs web dapat mengelompokkan halaman situs menjadi direktori dan sub direktori, yang memudahkan navigasi pengguna.
    . Mendukung Search Engine Optimization (SEO). URL yang ringkas dan bersih cenderung diberi peringkat tinggi pada mesin pencari seperti Google.

2. **What is the Domain Name System (DNS), and why is it essential for internet functionality?**  

    DNS (Domain Name System) adalah komponen protokol standar internet yang mengubah nama domain yang udah dipahami user menjadi internet protokol (IP). DNS memungkinkan user untuk terhubung dengan situs web menggunakan domain, bukan IP address. Daripada pengguna mengingat server "8.8.8.8" misalnya, penggunakan cukup mengingat google.com untuk mengkakses web google yang diinginkan user. 

3. **How does DNS translate a domain name into an IP address?**  

    Ketika user memasukkan nama domain di browser, komputer akan mengirimkan request ke DNS Server untuk mendapatkan IP address yang sesuai dengan nama domain tersebut. DNS Server kemudian merespons request dengan mengirimkan alamat IP yang tepat kepada komputer user.

4. **What is a hyperlink, and how does it assist in web navigation?**  

    Hyperlink adalah metode yang digunakan untuk mengakses halaman pada website. 

5. **Why are hyperlinks significant in web scraping tasks?**  

    . hyperlink digunakan untuk perpindahan halaman website
    . data detail umumnya disimpan dalam halaman tertentu yang dapat diakses melalui hyperlink
    . untuk melakukan browsing seluruh halaman website
    . web scraping umumnya mengumpulkan data hyperlink suatu website

6. **What is a web server, and how does it support website hosting?**  

    Web server adalah sebuah software yang berfungsi untuk menerima request HTTP atau HTTPS dari browser klien, lalu mengirimkan respons atas request tersebut kepada client dalam bentuk halaman website

7. **How does a web server process incoming requests from users or web scrapers?**  

    Browser klien melakukan request ke web server, data request akan disimpan pada Transmission Control Protocol (TCP), kemudian data request akan dikirim menuju ke alamat website tujuan.Jika request ditemukan, browser akan menampilkan data server dalam bentuk halaman, konten website atau berkas pada browser klien. Jika request data tidak ditemukan, web server akan menolak request dan menampilkan "Error 404".

8. **How do DNS, URLs, and hyperlinks work together to enable web navigation?**  

    User memasukkan URL, contoh google.com, kemudian request URL akan dikirim ke DNS server, kemudian DNS server akan menampilkan halaman konten website yang berisi hyperlink, kemudian user melakukan browsing halaman website melalui hyperlink yang ada di halaman website 

9. **Why is understanding web servers crucial for effective web scraping?**  

    Jika web scraper memahami web server, proses scraping akan efektif dan efisien, contohnya menghindari blokir website, dapat menghemat bandwith dengan menscraping data tertentu saja dan sebagainya

10. **How can analyzing the structure of URLs and hyperlinks improve the efficiency of web scraping?**  

   Dengan memahami struktur url dan hyperlink, scraper bisa selektif mengambil data yang diperlukan saja, sehingga ukuran data yang dikirim lebih kecil, hemat bandwith, dan cepat dalam proses scraping. 
