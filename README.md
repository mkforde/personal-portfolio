# Michael Forde - Personal Portfolio

[![Hugo Version](https://img.shields.io/static/v1?label=HUGO&message=v0.147.7+extended&color=blue&logo=hugo)](https://gohugo.io/)
[![Theme](https://img.shields.io/badge/theme-Hugo%20Noir-blue)](https://github.com/prxshetty/hugo-noir)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Live Site](https://img.shields.io/badge/live%20site-michaelforde.com-blue)](https://michaelforde.com)

A modern, responsive personal portfolio website built with Hugo and the Hugo Noir theme. Features a clean design, dark/light mode support, and showcases my experience, projects, and blog posts.

## 🌟 Features

- **Responsive Design** - Optimized for all devices and screen sizes
- **Dark & Light Mode** - Manual toggle with OS preference detection
- **Fast Performance** - Built with Hugo for lightning-fast loading
- **Professional Layout** - Clean, minimalist design focused on content
- **Tech Stack Showcase** - Interactive carousel displaying technical skills
- **Blog Integration** - Links to my tech blog at [blog.michaelforde.com](https://blog.michaelforde.com)
- **Experience Timeline** - Professional experience with company links
- **Project Portfolio** - Showcase of development projects
- **Contact Information** - Professional contact methods
- **Local Time Display** - Real-time local time in header
- **SEO Optimized** - Built-in SEO features and sitemap generation

## 🚀 Live Demo

Visit my portfolio at: **[michaelforde.com](https://michaelforde.com)**

## 🛠️ Built With

- **[Hugo](https://gohugo.io/)** - The world's fastest static site generator
- **[Hugo Noir Theme](https://github.com/prxshetty/hugo-noir)** - Clean, minimalistic theme
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[Go Modules](https://golang.org/ref/mod)** - Dependency management

## 📁 Project Structure

```
personal-portfolio/
├── content/                 # Site content
│   ├── about.md            # About page
│   ├── blogs.md            # Blog listing page
│   ├── contact.md          # Contact page
│   ├── experience.md       # Experience page
│   └── projects.md         # Projects page
├── data/                   # Data files for dynamic content
│   └── en/                # English language data
│       ├── author.toml     # Author information
│       ├── blogs.toml      # Blog posts data
│       ├── experience.toml # Professional experience
│       ├── organizations.toml # Organizations & roles
│       └── projects.toml   # Project information
├── layouts/                # Custom layout overrides
│   ├── _default/          # Default page layouts
│   ├── index.html         # Homepage layout
│   └── partials/          # Reusable components
├── scripts/                # Utility scripts
│   ├── deploy.sh          # Deployment script
│   └── blog_to_toml.py    # Blog data converter
├── themes/                 # Hugo themes
│   └── hugo-noir/         # Hugo Noir theme (submodule)
├── hugo.toml              # Hugo configuration
└── .gitignore             # Git ignore rules
```

## 🚀 Getting Started

### Prerequisites

- **Hugo Extended** version 0.92.0 or newer
- **Git** for version control
- **Go** 1.18+ (for Hugo)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/personal-portfolio.git
   cd personal-portfolio
   ```

2. **Initialize and update submodules**
   ```bash
   git submodule update --init --recursive
   ```

3. **Install Hugo** (if not already installed)
   ```bash
   # macOS with Homebrew
   brew install hugo
   
   # Or download from https://gohugo.io/installation/
   ```

4. **Run the development server**
   ```bash
   hugo server -D
   ```

5. **Open your browser**
   Navigate to `http://localhost:1313`

## ⚙️ Configuration

### Site Configuration (`hugo.toml`)

The main configuration file contains:
- Site metadata (title, description, base URL)
- Theme settings
- Menu configuration
- Build parameters

### Content Management

#### Adding New Pages
Create new `.md` files in the `content/` directory:

```markdown
---
title: "Page Title"
date: 2023-03-15T10:30:00+05:30
draft: false
layout: "default"
description: "Page description for SEO"
---
```

#### Managing Experience Data
Edit `data/en/experience.toml` to update professional experience:

```toml
[[experience]]
company = "Company Name"
role = "Job Title"
period = "Start Date - End Date"
description = "Role description"
responsibilities = [
    "Responsibility 1",
    "Responsibility 2"
]
```

#### Managing Projects
Edit `data/en/projects.toml` to showcase projects:

```toml
[[projects]]
title = "Project Name"
description = "Project description"
tech = "Technology stack"
image = "/images/projects/project.png"
link = "https://github.com/username/project"
```

## 🎨 Customization

### Theme Modifications
The Hugo Noir theme has been customized with:
- Custom color schemes
- Enhanced typography
- Improved mobile navigation
- Local time display
- Tech stack carousel animations

### Adding Custom Styles
Create `assets/css/custom.css` for additional styling:

```css
/* Your custom CSS here */
.custom-class {
    /* Custom styles */
}
```

### Layout Overrides
To override theme layouts, copy files from `themes/hugo-noir/layouts/` to your site's `layouts/` directory and modify them.

## 📝 Content Guidelines

### Blog Posts
- Use clear, descriptive titles
- Include relevant tags for categorization
- Write engaging summaries
- Link to external resources when appropriate

### Projects
- Provide clear project descriptions
- List all technologies used
- Include links to live demos and source code
- Add high-quality project images

### Experience
- Focus on achievements and impact
- Use action verbs and specific metrics
- Include relevant technologies and tools
- Keep descriptions concise but informative

## 🚀 Deployment

### Automated Deployment
The repository includes a deployment script (`scripts/deploy.sh`) that:
- Syncs the built site to a remote server
- Creates timestamped releases
- Updates the live site atomically
- Maintains deployment history

### Manual Deployment
1. Build the site: `hugo`
2. Upload the `public/` directory to your web server
3. Configure your web server to serve the static files

## 🔧 Development

### Local Development
```bash
# Start development server with live reload
hugo server -D

# Build for production
hugo

# Build with specific environment
hugo --environment production
```

### Adding Dependencies
```bash
# Add Go modules
go mod tidy
go mod download
```

## 📚 Resources

- **[Hugo Documentation](https://gohugo.io/documentation/)** - Official Hugo docs
- **[Hugo Noir Theme](https://github.com/prxshetty/hugo-noir)** - Theme documentation
- **[Tailwind CSS](https://tailwindcss.com/docs)** - CSS framework docs
- **[My Tech Blog](https://blog.michaelforde.com)** - Technical articles and tutorials

## 🤝 Contributing

While this is a personal portfolio, I welcome:
- Bug reports and feature suggestions
- Documentation improvements
- Performance optimizations
- Accessibility enhancements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Pranam Shetty](https://github.com/prxshetty)** - Creator of the Hugo Noir theme
- **[Hugo Team](https://gohugo.io/)** - For the amazing static site generator
- **[Tailwind CSS](https://tailwindcss.com/)** - For the utility-first CSS framework

---

**Built with ❤️ using Hugo and the Hugo Noir theme**
