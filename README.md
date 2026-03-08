# 🛡️ SafeGuard-AI-Compliance
> **The Ethical & Legal Shield for Next-Gen AI.** > *الدرع الأخلاقي والقانوني للجيل القادم من الذكاء الاصطناعي.*

---

## 🌟 Overview | نظرة عامة
**SafeGuard-AI** is an advanced middleware designed to ensure that AI interactions remain safe, legal, and respectful. It bridges the gap between powerful LLMs and global regulatory standards.

مشروع **SafeGuard-AI** هو طبقة برمجية وسيطة متطورة تهدف لضمان بقاء تفاعلات الذكاء الاصطناعي آمنة، قانونية، ومحترمة. يعمل كجسر يربط بين النماذج اللغوية الكبيرة والمعايير التنظيمية العالمية.

---

## 🛠️ Core Pillars | الركائز الأساسية

### ⚖️ 1. Legal Compliance | الامتثال القانوني
* **EU AI Act:** Strictly follows European regulations to prevent emotional manipulation and high-risk AI behaviors.  
    *(الالتزام بقانون الذكاء الاصطناعي الأوروبي لمنع التلاعب السلوكي).*
* **US Cyber Laws:** Blocks any requests related to cybercrimes, hacking, or unauthorized data access.  
    *(التصدي لمحاولات الجرائم الإلكترونية والاختراق وفق القوانين الأمريكية).*

### 🚫 2. Ethical Guardrails | الضوابط الأخلاقية
* **Profanity Filter:** Real-time detection and blocking of vulgar language and insults.  
    *(نظام فحص فوري للألفاظ النابية والشتائم).*
* **Hate Speech Detection:** Prevents any form of discrimination or inflammatory content.  
    *(منع خطاب الكراهية والتمييز بكافة أشكاله).*

### 🤝 3. Community Standards | معايير المجتمع
* Maintains a professional and respectful dialogue environment for all users.  
    *(الحفاظ على بيئة نقاش مهنية ومحترمة لجميع المستخدمين).*

---

## 🚀 How it Works | كيف يعمل؟
The system acts as a **'Gatekeeper'** (حارس بوابة) between the user and the AI:

1.  **Input Interception:** Scans the user's prompt for legal/ethical violations.  
    *(اعتراض المدخلات وفحصها من المخالفات).*
2.  **Logic Validation:** Matches the intent against US/EU legal datasets.  
    *(مطابقة النية مع قواعد البيانات القانونية الدولية).*
3.  **Sanitized Output:** Delivers a safe response or blocks the violation.  
    *(تقديم إجابة "نظيفة" أو حجب المحتوى المخالف).*

---
AI-Safety-Platform
│
├── gateway/
│   └── llm_firewall.py
│
├── moderation/
│   ├── prompt_attack_detector.py
│   ├── toxicity_detector.py
│   ├── language_detector.py
│   └── contextual_reasoning.py
│
├── pipeline/
│   └── realtime_pipeline.py
│
├── api/
│   └── moderation_api.py
│
├── dashboard/
│   ├── backend/
│   │   └── admin_api.py
│   └── frontend/
│       └── dashboard.html
│
├── models/
│   └── ml_models.py
│
├── data/
│   └── policies.json
│
├── logs/
│   └── moderation_logs.db
│
├── requirements.txt
└── main.py

### 📂 Project Structure | هيكل المشروع

The project follows a **Modular Security Architecture** to ensure scalability and high-performance moderation.

يعتمد المشروع على **بنية هندسية مجزأة** لضمان القابلية للتوسع والأداء العالي في عمليات الإشراف الذكي.

* **`📁 gateway/`**: The first line of defense; acts as a firewall for incoming LLM prompts.
* *(خط الدفاع الأول؛ يعمل كجدار حماية للمدخلات قبل معالجتها).*


* **`📁 moderation/`**: The core intelligence engine containing specific detectors:
* **`prompt_attack_detector.py`**: Defends against Jailbreak and Injection attacks.
* **`toxicity_detector.py`**: Filters profanity, hate speech, and harassment.
* **`contextual_reasoning.py`**: Maps inputs against EU/US legal frameworks.
* *(المحرك الأساسي الذي يضم كواشف الهجمات، السمية، والربط القانوني).*


* **`📁 pipeline/`**: Coordinates the flow between different moderation modules in real-time.
* *(منظم التدفق الذي يربط وحدات الإشراف المختلفة في الوقت الفعلي).*


* **`📁 api/`**: Provides RESTful endpoints to integrate the platform with other applications.
* *(واجهة برمجة التطبيقات لربط المنصة بالتطبيقات الأخرى).*


* **`📁 dashboard/`**: A management interface (Frontend & Backend) to monitor logs and policies.
* *(لوحة تحكم لمراقبة السجلات وإدارة السياسات).*


* **`📁 models/`**: Contains the logic for machine learning models used in detection.
* *(يحتوي على المنطق الخاص بنماذج تعلم الآلة المستخدمة).*


* **`📁 data/`**: Storage for `policies.json` (The legal/ethical constitution of the bot).
* *(مستودع السياسات والقوانين والقواعد الأخلاقية).*


* **`📁 logs/`**: Database and files for tracking all moderation activities and violations.
* *(قاعدة بيانات لتتبع كافة الأنشطة والمخالفات).*

---

### 💡 Why this structure? | لماذا هذا الهيكل؟

As a **Computer and Software Engineering student**, I designed this layout to achieve **Decoupling**: separating the legal logic from the core AI processing. This allows for easy updates to laws (like the EU AI Act) without breaking the main system.

بصفتي **طالباً في هندسة الحاسوب والبرمجيات**، صممت هذا الهيكل لتحقيق **فك الارتباط (Decoupling)** بين المنطق القانوني ومعالجة الذكاء الاصطناعي. هذا يسمح بتحديث القوانين بسهولة دون التأثير على استقرار النظام الأساسي.

---
## 👨‍💻 Tech Stack | التقنيات المستخدمة
* **Language:** Python 🐍
* **AI Engine:** OpenAI GPT-4o / Local LLMs.
* **Frameworks:** Pydantic (Data Validation), Natural Language Processing (NLP).

---
## 🌱 About the Developer | نبذة عن المطور

This project is one of my **first experiences** in the field of AI Ethics and Compliance. I am currently a **4th-year Computer Engineering student** and a **2nd-year Software Engineering student**. I am deeply passionate about building technology that serves humanity safely. I am continuously learning and look forward to evolving this project and my skills further, Insha'Allah.

هذا المشروع هو واحد من **أولى تجاربي** في مجال أخلاقيات وامتثال الذكاء الاصطناعي. أنا حالياً طالب في **السنة الرابعة هندسة حاسوب** وطالب في **السنة الثانية هندسة برمجيات**. لدي شغف كبير ببناء تقنيات تخدم البشرية بشكل آمن، وأنا في رحلة تعلم مستمرة وآمل أن أطور هذا المشروع ومهاراتي بشكل أكبر مستقبلاً، إن شاء الله.

---
**Developed with ❤️ by Hamed Hazem Kuheil.**
*Bridging Computer & Software Engineering for a safer AI.*

## 🤝 Contribution & License
* **Contribution:** We welcome developers and legal experts! Feel free to Fork and submit a PR.
* **License:** Licensed under the **MIT License**.

---
**Developed with ❤️ by Hamed Hazem Kuheil.** *Making AI safer, one step at a time.*
****hamedkuheil@yahoo.com