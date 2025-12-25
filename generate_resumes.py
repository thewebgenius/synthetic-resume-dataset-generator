import json
import random
import uuid

# Set seed for reproducibility
random.seed(42)

# -------------------------------
# DATA POOLS
# -------------------------------

NAMES = [
    "Rohit Verma", "Amit Sharma", "Priya Patel", "Ankit Singh", "Neha Gupta",
    "Arjun Kumar", "Sneha Reddy", "Vikram Mehta", "Pooja Iyer", "Karan Joshi"
]

EMAIL_DOMAINS = ["gmail.com", "outlook.com", "yahoo.com", "protonmail.com"]

JOB_TITLES = [
    "Machine Learning Engineer",
    "Computer Vision Engineer", 
    "Deep Learning Engineer",
    "AI/ML Engineer",
    "Data Scientist"
]

SUMMARIES = [
    "Machine Learning Engineer with hands-on experience in building CNN-based computer vision systems, model optimization, and deployment. Strong background in Python, PyTorch, and applied deep learning.",
    "Computer Vision Engineer specializing in image processing and deep learning. Experienced in developing production-ready CV systems using PyTorch and TensorFlow with focus on real-time inference.",
    "Deep Learning Engineer with expertise in neural network architectures, model training, and optimization. Proven track record in reducing inference time and improving model accuracy.",
    "AI/ML Engineer focused on developing end-to-end machine learning pipelines. Strong foundation in computer vision, transfer learning, and cloud deployment strategies.",
    "Data Scientist with specialization in computer vision and deep learning. Experienced in building CNN models for image classification, object detection, and semantic segmentation."
]

DEGREES = [
    ("B.Tech", "Computer Science"),
    ("B.Tech", "Information Technology"),
    ("B.Tech", "Artificial Intelligence and Data Science"),
    ("B.Sc", "Computer Science")
]

INSTITUTIONS = [
    "National Institute of Engineering",
    "Indian Institute of Technology",
    "Delhi Technological University",
    "Birla Institute of Technology",
    "VIT University"
]

# Skills categorized
PROGRAMMING_SKILLS = ["Python", "C++", "Java", "JavaScript", "SQL"]
ML_DL_SKILLS = [
    "CNN", "Transfer Learning", "PyTorch", "TensorFlow", "Keras",
    "YOLO", "ResNet", "VGG", "Image Segmentation", "Object Detection"
]
CV_SKILLS = [
    "OpenCV", "Image Augmentation", "PIL/Pillow", "scikit-image",
    "Image Processing", "Feature Extraction"
]
TOOLS = ["Git", "Docker", "Linux", "Jupyter", "AWS", "Azure", "MLflow", "DVC"]

# Experience details
COMPANIES = [
    "Tech Solutions Pvt Ltd",
    "AI Innovations Inc",
    "DataCore Systems",
    "Vision Tech Labs",
    "CloudML Solutions"
]

ROLES = [
    "Machine Learning Intern",
    "Computer Vision Intern", 
    "Deep Learning Intern",
    "AI Research Intern"
]

EXPERIENCE_BULLETS = [
    "Developed CNN-based image classification models achieving {acc}% validation accuracy",
    "Implemented data augmentation pipeline improving model generalization by {imp}%",
    "Assisted in model deployment using Docker and achieved {perf}ms inference time",
    "Optimized model architecture reducing parameters by {red}% while maintaining accuracy",
    "Built end-to-end ML pipeline from data preprocessing to model serving",
    "Collaborated with cross-functional team of {team} engineers on CV projects",
    "Reduced model training time by {time}% through efficient data loading",
    "Implemented transfer learning using pre-trained ResNet achieving {acc}% accuracy"
]

# Project details
PROJECTS = [
    {
        "title": "Face Recognition System",
        "bullets": [
            "Designed a CNN-based face recognition pipeline using PyTorch",
            "Trained on {data}k+ images with augmentation and achieved {acc}% accuracy",
            "Implemented real-time inference with {fps} FPS on CPU"
        ]
    },
    {
        "title": "Plant Disease Detection",
        "bullets": [
            "Built image classification model to detect {classes} crop diseases",
            "Reduced false negatives by {imp}% through class balancing",
            "Deployed model as REST API using Flask with {ms}ms response time"
        ]
    },
    {
        "title": "Object Detection System",
        "bullets": [
            "Implemented YOLOv5 for real-time object detection",
            "Achieved {map} mAP on custom dataset of {data}k images",
            "Optimized for edge deployment achieving {fps} FPS on Raspberry Pi"
        ]
    },
    {
        "title": "Image Segmentation Pipeline",
        "bullets": [
            "Developed U-Net based semantic segmentation model",
            "Achieved {iou}% IoU score on medical imaging dataset",
            "Processed {data}k+ images with automated preprocessing pipeline"
        ]
    },
    {
        "title": "Document Scanner OCR",
        "bullets": [
            "Built CNN-based document detection and text extraction system",
            "Integrated Tesseract OCR achieving {acc}% character accuracy",
            "Processed {data}+ documents with automated quality checks"
        ]
    },
    {
        "title": "Deepfake Detection System",
        "bullets": [
            "Trained CNN model to detect manipulated images and videos",
            "Achieved {acc}% detection accuracy on benchmark dataset",
            "Implemented real-time video analysis at {fps} FPS"
        ]
    }
]

HOBBIES = [
    "Contributing to Open Source ML Projects",
    "Reading Research Papers on Computer Vision",
    "Competitive Programming",
    "Photography and Image Processing",
    "Building Side Projects with AI",
    "Tech Blogging about Deep Learning"
]

# -------------------------------
# RESUME GENERATOR
# -------------------------------

def fill_template(text, **kwargs):
    """Fill template placeholders with random values"""
    for key, value in kwargs.items():
        text = text.replace(f"{{{key}}}", str(value))
    return text

def generate_resume():
    name = random.choice(NAMES)
    first_name = name.split()[0].lower()
    last_name = name.split()[1].lower()
    email = f"{first_name}.{last_name}@{random.choice(EMAIL_DOMAINS)}"
    phone = f"+91-{random.randint(7000000000, 9999999999)}"
    
    # LinkedIn and GitHub
    linkedin = f"linkedin.com/in/{first_name}-{last_name}"
    github = f"github.com/{first_name}{last_name}"
    
    resume = {
        "personal_info": {
            "name": name,
            "job_title": random.choice(JOB_TITLES),
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "github": github
        },
        "summary": random.choice(SUMMARIES),
        "education": [
            {
                "degree": random.choice(DEGREES)[0],
                "field": random.choice(DEGREES)[1],
                "institution": random.choice(INSTITUTIONS),
                "start_year": "2021",
                "end_year": "2025"
            }
        ],
        "skills": {
            "programming": random.sample(PROGRAMMING_SKILLS, random.randint(3, 4)),
            "ml_dl": random.sample(ML_DL_SKILLS, random.randint(4, 6)),
            "cv": random.sample(CV_SKILLS, random.randint(3, 4)),
            "tools": random.sample(TOOLS, random.randint(4, 6))
        },
        "projects": [],
        "experience": [],
        "hobbies": random.sample(HOBBIES, random.randint(2, 3))
    }

    # Add 2-3 projects with detailed bullets
    num_projects = random.randint(2, 3)
    selected_projects = random.sample(PROJECTS, num_projects)
    
    for project_template in selected_projects:
        project = {
            "title": project_template["title"],
            "description": []
        }
        
        # Fill in template bullets with random metrics
        for bullet_template in project_template["bullets"]:
            bullet = fill_template(
                bullet_template,
                acc=random.randint(88, 96),
                data=random.randint(5, 15),
                imp=random.randint(15, 30),
                ms=random.randint(50, 200),
                fps=random.randint(25, 60),
                classes=random.randint(5, 10),
                map=random.randint(75, 90),
                iou=random.randint(82, 94),
                red=random.randint(30, 50),
                perf=random.randint(10, 50),
                team=random.randint(3, 8),
                time=random.randint(20, 40)
            )
            project["description"].append(bullet)
        
        resume["projects"].append(project)

    # Add experience (70% chance)
    if random.random() > 0.3:
        exp_bullets = []
        num_bullets = random.randint(3, 4)
        
        for bullet_template in random.sample(EXPERIENCE_BULLETS, num_bullets):
            bullet = fill_template(
                bullet_template,
                acc=random.randint(88, 95),
                imp=random.randint(12, 25),
                red=random.randint(25, 45),
                perf=random.randint(15, 50),
                team=random.randint(3, 7),
                time=random.randint(25, 40)
            )
            exp_bullets.append(bullet)
        
        resume["experience"] = exp_bullets
    else:
        resume["experience"] = []

    return resume

# -------------------------------
# SAVE RESUMES
# -------------------------------

def save_resumes(n=5):
    print(f"Generating {n} resumes...")
    for i in range(n):
        resume = generate_resume()
        file_name = f"{uuid.uuid4()}.json"
        with open(f"data/resumes/{file_name}", "w") as f:
            json.dump(resume, f, indent=4)
        
        if (i + 1) % 100 == 0:
            print(f"  Generated {i + 1}/{n} resumes...")
    
    print(f"✓ All {n} resumes generated successfully!")

if __name__ == "__main__":
    save_resumes(1000)
