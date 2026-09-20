import { ExternalLink } from "lucide-react"
import { Button } from "@/components/ui/button"

const projects = [
  {
    title: "Online Board Game for HCI Research",
    description:
      "Developed an interactive online board game platform to support Human-Computer Interaction research, enabling data collection on user behavior and interaction patterns.",
    technologies: ["JavaScript", "React", "Node.js", "WebSocket"],
    outcome: "Successfully deployed for research study with 100+ participants",
  },
  {
    title: "Data Analysis & Predictive Modeling",
    description:
      "Built predictive models using machine learning techniques to analyze large datasets and generate actionable business insights for decision-making.",
    technologies: ["Python", "Pandas", "Scikit-learn", "Tableau"],
    outcome: "Improved prediction accuracy by 25% over baseline models",
  },
  {
    title: "Mobile Application Development Capstone",
    description:
      "Led a team to design and develop a cross-platform mobile application focusing on user experience and seamless integration with backend services.",
    technologies: ["Swift", "iOS", "Firebase", "REST APIs"],
    outcome: "Delivered MVP with core features within 3-month timeline",
  },
]

export function ProjectsSection() {
  return (
    <section id="projects" className="py-24 px-6">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-12">
          Selected Projects
        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.map((project) => (
            <article
              key={project.title}
              className="group bg-card rounded-xl border border-border p-6 hover:border-primary/50 hover:shadow-lg hover:shadow-primary/5 transition-all duration-300"
            >
              <div className="space-y-4">
                <h3 className="text-xl font-semibold text-foreground group-hover:text-primary transition-colors">
                  {project.title}
                </h3>

                <p className="text-muted-foreground text-sm leading-relaxed">
                  {project.description}
                </p>

                <div className="flex flex-wrap gap-2">
                  {project.technologies.map((tech) => (
                    <span
                      key={tech}
                      className="text-xs px-2.5 py-1 rounded-full bg-primary/10 text-primary font-medium"
                    >
                      {tech}
                    </span>
                  ))}
                </div>

                <div className="pt-2 border-t border-border">
                  <p className="text-sm text-muted-foreground">
                    <span className="font-medium text-foreground">Outcome:</span>{" "}
                    {project.outcome}
                  </p>
                </div>

                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full mt-2 group/btn"
                >
                  View Details
                  <ExternalLink className="ml-2 h-4 w-4 transition-transform group-hover/btn:translate-x-1" />
                </Button>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}
