## **Instructions**  
**Objective:** The goal of this exercise is to help you develop a foundational understanding of computer networks, specifically focusing on TCP/IP and the OSI model, which are critical for understanding how data is transmitted over networks.

By the end of this exercise, you will have a clear understanding of the fundamental concepts of networking, which will aid in troubleshooting network issues and improving your overall knowledge of web scraping and other network-related tasks. 🚀  

---

## **Questions**  
1. **What is TCP/IP, and why is it important for computer networks?**  

    TCP/IP adalah Transmission Control Protocol/Internet Protocol. TCP/IP adalah serangkaian protokol (aturan) yang menghubungkan perangkat jaringan melalui internet. TCP/IP mencakup : Hypertext Transfer Protocol (HTTP), HTTP Secure, dan File Transfer Protocol. TCP/IP dibutuhkan karena dapat menghubungkan komputer dalam jaringan, tanpa TCP/IP proses komunikasi komputer tidak terstruktur dan tidak efisien.

2. **What are the main functions of TCP in a network?**  

    TCP memastikan pengiriman data yang terurut. Setiap segmen data diberi nomor urutan (sequence number) untuk memastikan bahwa segmen-segmen tersebut diterima dan diurutkan dengan benar di sisi penerima. Ini penting dalam menjaga integritas data dan memastikan data diproses dalam urutan yang benar oleh aplikasi penerima

3. **What role does IP play in a computer network?**  

   IP address adalah identitas suatu komputer dalam jaringan. IP address berfungsi sebagai alamat pengiriman data ke komputer yang diinginkan

4. **What is the difference between TCP and UDP, and when would you use each?**  

    TCP adalah Transfer Control Protocol. UDP adalah User Datagram Protocol. UDP adalah protokol transport yang digunakan dalam komunikasi data jaringan komputer. Protokol UDP cocok untuk aplikasi yang membutuhkan kecepatan tinggi dan responsivitas besar. Namun kekurangan UDP adalah seringkali terjadi paket hilang saat transit dan menumbulkan serangan DDoS. TCP memerlukan koneksi ke server untuk terhubung, sedangkan UDP memungkinkan pengiriman data peer to peer tanpa server pusat.  

5. **What is the OSI model, and why is it important in networking?**  

    OSI (Open System Interconnection) adalah standar proses komunikasi komputer dalam jaringan. OSI model diciptakan oleh ISO (International Organization for Standarization). Dahulu komunikasi komputer dalam jaringan memiliki standar format data dan protokol yang berbeda-beda, sehingga ISO menciptakan model yang standar untuk komunikasi komputer dalam jaringan.

6. **What is the first layer of the OSI model, and what is its function?**  

    Layer 1 OSI adalah physical layer. Physical layer mentransmisikan data dalam bentuk data biner. Peralatan seperti repeater, hub dan network card berada pada layer ini 

7. **What does the transport layer (Layer 4) of the OSI model do?**  

    Transport layer mengirim  paket data ke tujuan, memastikan data terkirim atau tidak. Transport layer menggunakan protokol TCP atau UDP.

8. **What is the network layer (Layer 3) of the OSI model, and how does it work?**  

    Network layer mendefinisikan alamat IP dan menyediakan fungsi routing, sehingga paket data dapat dikirim dari network lokal menuju network lain atau mendefinisikan network yang sama. 

9. **What is the role of the application layer (Layer 7) in the OSI model?**  

    Application layer adalah antarmuka yang menghubungkan user dengan fungsionalitas jaringan. Protokol yang berada dalam lapisan ini adalah HTTP, FTP, SMTP, dan NFS. 

10. **How does understanding TCP/IP and the OSI model help in troubleshooting network issues?**  

    Dengan memahami TCP/IP dan OSI layer dapat mengidentifikasi kendala scraping berada di layer mana, sehingga dapat mengatasi kendala scraping lebih akurat,