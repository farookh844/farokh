<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMU Medical Entrance Hub - Paramedical & Nursing Preparation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        body {
            font-family: 'Poppins', sans-serif;
        }
        .hero-gradient {
            background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        }
        .news-ticker {
            animation: ticker 20s linear infinite;
        }
        @keyframes ticker {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        .testimonial-card {
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .testimonial-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px -10px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body class="bg-gray-50">
    <!-- Top Bar -->
    <div class="bg-blue-900 text-white py-2 px-4 text-sm">
        <div class="container mx-auto flex justify-between items-center">
            <div class="flex space-x-4">
                <span><i class="fas fa-phone-alt mr-1"></i> +91 8279839726</span>
                <span><i class="fas fa-envelope mr-1"></i> farookhumarkhan222@gmail.com</span>
            </div>
            <div class="flex space-x-4">
                <a href="#" class="hover:text-blue-200"><i class="fab fa-facebook-f"></i></a>
                <a href="https://instagram.com/farookh_umar_khan" class="hover:text-blue-200"><i class="fab fa-instagram"></i></a>
                <a href="#" class="hover:text-blue-200"><i class="fab fa-youtube"></i></a>
                <a href="https://wa.me/918279839726" class="hover:text-blue-200"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
    </div>

    <!-- Navigation -->
    <nav class="bg-white shadow-md sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <div class="bg-blue-600 text-white p-2 rounded-lg">
                    <i class="fas fa-user-md text-xl"></i>
                </div>
                <span class="text-xl font-bold text-blue-900">AMU Medical Hub</span>
            </div>
            
            <div class="hidden md:flex space-x-6">
                <a href="#" class="text-blue-900 font-medium hover:text-blue-600">Home</a>
                <a href="#" class="text-gray-700 hover:text-blue-600">Courses</a>
                <a href="#" class="text-gray-700 hover:text-blue-600">Mock Tests</a>
                <a href="#" class="text-gray-700 hover:text-blue-600">Resources</a>
                <a href="#" class="text-gray-700 hover:text-blue-600">Blog</a>
                <a href="#" class="text-gray-700 hover:text-blue-600">Contact</a>
            </div>
            
            <div class="flex items-center space-x-4">
                <a href="#" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-medium transition duration-300">Login</a>
                <button class="md:hidden focus:outline-none">
                    <i class="fas fa-bars text-gray-700 text-xl"></i>
                </button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-gradient text-white py-16 md:py-24">
        <div class="container mx-auto px-4 flex flex-col md:flex-row items-center">
            <div class="md:w-1/2 mb-10 md:mb-0">
                <h1 class="text-4xl md:text-5xl font-bold mb-6 leading-tight">Prepare for AMU Paramedical & Nursing 2025</h1>
                <p class="text-xl mb-8 text-blue-100">Comprehensive preparation platform with mock tests, study materials, and expert guidance for AMU medical entrance exams.</p>
                
                <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
                    <a href="#" class="bg-white text-blue-900 hover:bg-gray-100 px-6 py-3 rounded-lg font-bold text-center transition duration-300">Apply Now</a>
                    <a href="#" class="bg-transparent border-2 border-white hover:bg-white hover:text-blue-900 px-6 py-3 rounded-lg font-bold text-center transition duration-300">Free Mock Test</a>
                </div>
            </div>
            
        </div>
    </section>

    <!-- News Ticker -->
    <div class="bg-blue-800 text-white py-2 overflow-hidden">
        <div class="container mx-auto px-4 flex items-center">
            <div class="bg-blue-600 px-3 py-1 rounded mr-4 whitespace-nowrap">
                <i class="fas fa-bullhorn mr-2"></i> Latest Updates
            </div>
            <div class="flex-1 overflow-hidden">
                <div class="news-ticker whitespace-nowrap">
                    <span class="mr-8">AMU releases tentative exam schedule for 2025 admissions</span>
                    <span class="mr-8">New batch of crash course starting from 15th July</span>
                    <span class="mr-8">Download last 5 years question papers from our resources section</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Courses Highlights -->
    <section class="py-16 bg-white">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-12">Our Courses</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Course 1 -->
                <div class="bg-gray-50 rounded-xl overflow-hidden border border-gray-200 hover:shadow-lg transition duration-300">
                    <div class="bg-blue-600 text-white p-4">
                        <h3 class="text-xl font-bold">B.Sc. Nursing</h3>
                    </div>
                    <div class="p-6">
                        <p class="text-gray-600 mb-4">4-year undergraduate program preparing students for professional nursing practice.</p>
                        <ul class="space-y-2 mb-6">
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Duration: 4 Years</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Seats: 60</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Eligibility: 10+2 with Science</span>
                            </li>
                        </ul>
                        <a href="#" class="text-blue-600 font-medium hover:text-blue-800 flex items-center">
                            View Details <i class="fas fa-arrow-right ml-2"></i>
                        </a>
                    </div>
                </div>
                
                <!-- Course 2 -->
                <div class="bg-gray-50 rounded-xl overflow-hidden border border-gray-200 hover:shadow-lg transition duration-300">
                    <div class="bg-blue-600 text-white p-4">
                        <h3 class="text-xl font-bold">B.Sc. Medical Lab Technology</h3>
                    </div>
                    <div class="p-6">
                        <p class="text-gray-600 mb-4">3-year program focusing on laboratory diagnostics and clinical pathology.</p>
                        <ul class="space-y-2 mb-6">
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Duration: 3 Years</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Seats: 40</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Eligibility: 10+2 with PCB</span>
                            </li>
                        </ul>
                        <a href="#" class="text-blue-600 font-medium hover:text-blue-800 flex items-center">
                            View Details <i class="fas fa-arrow-right ml-2"></i>
                        </a>
                    </div>
                </div>
                
                <!-- Course 3 -->
                <div class="bg-gray-50 rounded-xl overflow-hidden border border-gray-200 hover:shadow-lg transition duration-300">
                    <div class="bg-blue-600 text-white p-4">
                        <h3 class="text-xl font-bold">B.Sc. Radiography</h3>
                    </div>
                    <div class="p-6">
                        <p class="text-gray-600 mb-4">3-year program in medical imaging techniques and radiation therapy.</p>
                        <ul class="space-y-2 mb-6">
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Duration: 3 Years</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Seats: 30</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span>Eligibility: 10+2 with PCB</span>
                            </li>
                        </ul>
                        <a href="#" class="text-blue-600 font-medium hover:text-blue-800 flex items-center">
                            View Details <i class="fas fa-arrow-right ml-2"></i>
                        </a>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-12">
                <a href="#" class="inline-block bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-bold transition duration-300">
                    View All Courses <i class="fas fa-arrow-right ml-2"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="py-16 bg-gray-50">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-12">Why Choose Our Platform?</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Feature 1 -->
                <div class="bg-white p-6 rounded-xl shadow-md text-center">
                    <div class="bg-blue-100 w-16 h-16 mx-auto rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-file-alt text-blue-600 text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Latest Syllabus</h3>
                    <p class="text-gray-600">Updated study materials based on the latest AMU entrance exam pattern and syllabus.</p>
                </div>
                
                <!-- Feature 2 -->
                <div class="bg-white p-6 rounded-xl shadow-md text-center">
                    <div class="bg-blue-100 w-16 h-16 mx-auto rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-laptop-code text-blue-600 text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Mock Tests</h3>
                    <p class="text-gray-600">Real-time exam simulation with detailed performance analysis and solutions.</p>
                </div>
                
                <!-- Feature 3 -->
                <div class="bg-white p-6 rounded-xl shadow-md text-center">
                    <div class="bg-blue-100 w-16 h-16 mx-auto rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-chalkboard-teacher text-blue-600 text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Expert Guidance</h3>
                    <p class="text-gray-600">Personalized mentorship from experienced faculty and successful alumni.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="py-16 bg-white">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-12">Success Stories</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Testimonial 1 -->
                <div class="testimonial-card bg-gray-50 p-6 rounded-xl border border-gray-200">
                    <div class="flex items-center mb-4">
                        <img src="https://randomuser.me/api/portraits/women/32.jpg" alt="Student" class="w-12 h-12 rounded-full mr-4">
                        <div>
                            <h4 class="font-bold">Ayesha Khan</h4>
                            <p class="text-blue-600 text-sm">B.Sc. Nursing (2023)</p>
                        </div>
                    </div>
                    <p class="text-gray-600 mb-4">"The mock tests here were exactly like the actual exam. I secured AIR 12 thanks to the thorough preparation."</p>
                    <div class="flex text-yellow-400">
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                    </div>
                </div>
                
                <!-- Testimonial 2 -->
                <div class="testimonial-card bg-gray-50 p-6 rounded-xl border border-gray-200">
                    <div class="flex items-center mb-4">
                        <img src="https://randomuser.me/api/portraits/men/45.jpg" alt="Student" class="w-12 h-12 rounded-full mr-4">
                        <div>
                            <h4 class="font-bold">Rahul Sharma</h4>
                            <p class="text-blue-600 text-sm">B.Sc. MLT (2022)</p>
                        </div>
                    </div>
                    <p class="text-gray-600 mb-4">"The study materials and previous year papers helped me understand the exam pattern thoroughly."</p>
                    <div class="flex text-yellow-400">
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                    </div>
                </div>
                
                <!-- Testimonial 3 -->
                <div class="testimonial-card bg-gray-50 p-6 rounded-xl border border-gray-200">
                    <div class="flex items-center mb-4">
                        <img src="https://randomuser.me/api/portraits/women/65.jpg" alt="Student" class="w-12 h-12 rounded-full mr-4">
                        <div>
                            <h4 class="font-bold">Priya Singh</h4>
                            <p class="text-blue-600 text-sm">B.Sc. Radiography (2024)</p>
                        </div>
                    </div>
                    <p class="text-gray-600 mb-4">"The faculty guidance helped me improve my weak areas and boost my confidence for the entrance exam."</p>
                    <div class="flex text-yellow-400">
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="py-16 bg-blue-900 text-white">
        <div class="container mx-auto px-4 text-center">
            <h2 class="text-3xl font-bold mb-6">Ready to Start Your Medical Journey?</h2>
            <p class="text-xl mb-8 max-w-2xl mx-auto text-blue-100">Join hundreds of successful students who aced their AMU medical entrance exams with our guidance.</p>
            
            <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
                <a href="#" class="bg-white text-blue-900 hover:bg-gray-100 px-8 py-3 rounded-lg font-bold transition duration-300">Enroll Now</a>
                <a href="#" class="bg-transparent border-2 border-white hover:bg-white hover:text-blue-900 px-8 py-3 rounded-lg font-bold transition duration-300">Talk to Counselor</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white pt-12 pb-6">
        <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <!-- About -->
                <div>
                    <h3 class="text-xl font-bold mb-4 flex items-center">
                        <div class="bg-blue-600 p-2 rounded-lg mr-2">
                            <i class="fas fa-user-md"></i>
                        </div>
                        AMU Medical Hub
                    </h3>
                    <p class="text-gray-400 mb-4">Your one-stop platform for AMU Paramedical and Nursing entrance exam preparation.</p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://instagram.com/farookh_umar_khan" class="text-gray-400 hover:text-white"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white"><i class="fab fa-youtube"></i></a>
                        <a href="https://wa.me/918279839726" class="text-gray-400 hover:text-white"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
                
                <!-- Quick Links -->
                <div>
                    <h3 class="text-lg font-bold mb-4">Quick Links</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white">Home</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Courses</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Mock Tests</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Study Materials</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Blog</a></li>
                    </ul>
                </div>
                
                <!-- Contact -->
                <div>
                    <h3 class="text-lg font-bold mb-4">Contact Us</h3>
                    <ul class="space-y-2">
                        <li class="flex items-start">
                            <i class="fas fa-map-marker-alt mt-1 mr-2 text-blue-400"></i>
                            <span class="text-gray-400">Muzzamil 23 VM Hall, AMU, Aligarh, UP, India</span>
                        </li>
                        <li class="flex items-start">
                            <i class="fas fa-phone-alt mt-1 mr-2 text-blue-400"></i>
                            <span class="text-gray-400">+91 8279839726</span>
                        </li>
                        <li class="flex items-start">
                            <i class="fas fa-envelope mt-1 mr-2 text-blue-400"></i>
                            <span class="text-gray-400">farookhumarkhan222@gmail.com</span>
                        </li>
                        <li class="flex items-start">
                            <i class="fas fa-map-marker-alt mt-1 mr-2 text-blue-400"></i>
                            <span class="text-gray-400">Muzzamil 23 VM Hall, AMU, Aligarh, UP, India</span>
                        </li>
                    </ul>
                </div>
                
                <!-- Newsletter -->
                <div>
                    <h3 class="text-lg font-bold mb-4">Newsletter</h3>
                    <p class="text-gray-400 mb-4">Subscribe to get updates on exam dates, preparation tips, and more.</p>
                    <form class="flex">
                        <input type="email" placeholder="Your email" class="bg-gray-800 text-white px-4 py-2 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500 w-full">
                        <button type="submit" class="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-r-lg">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </form>
                </div>
            </div>
            
            <div class="border-t border-gray-800 pt-6 flex flex-col md:flex-row justify-between items-center">
                <p class="text-gray-400 text-sm mb-4 md:mb-0">© 2023 AMU Medical Hub. All rights reserved.</p>
                <div class="flex space-x-4">
                    <a href="#" class="text-gray-400 hover:text-white text-sm">Privacy Policy</a>
                    <a href="#" class="text-gray-400 hover:text-white text-sm">Terms of Service</a>
                    <a href="#" class="text-gray-400 hover:text-white text-sm">Sitemap</a>
                </div>
            </div>
        </div>
    </footer>

</body>
</html>