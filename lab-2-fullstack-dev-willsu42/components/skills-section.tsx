const skillCategories = [
  {
    title: "Programming & Engineering",
    skills: ["Python", "JavaScript", "C#", "Java", "SQL", "R", "Swift"],
  },
  {
    title: "Systems & Data",
    skills: ["Database Design", "ERP Systems", "EDI", "Data Analysis", "ETL"],
  },
  {
    title: "Security & Infrastructure",
    skills: ["Cybersecurity", "APIs", "Firewalls", "Network Security", "Cloud Services"],
  },
  {
    title: "Product & Management",
    skills: [
      "Requirement Analysis",
      "Stakeholder Communication",
      "Documentation",
      "Agile/Scrum",
      "Project Planning",
    ],
  },
]

export function SkillsSection() {
  return (
    <section id="skills" className="py-24 px-6 bg-secondary/30">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-12">
          Skills & Tools
        </h2>

        <div className="grid md:grid-cols-2 gap-8">
          {skillCategories.map((category) => (
            <div key={category.title} className="space-y-4">
              <h3 className="text-lg font-semibold text-foreground">
                {category.title}
              </h3>
              <div className="flex flex-wrap gap-2">
                {category.skills.map((skill) => (
                  <span
                    key={skill}
                    className="px-4 py-2 rounded-lg bg-card border border-border text-sm text-muted-foreground hover:border-primary/50 hover:text-foreground transition-colors cursor-default"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
