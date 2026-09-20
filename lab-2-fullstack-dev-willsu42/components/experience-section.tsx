import { Briefcase } from "lucide-react"

const experiences = [
  {
    title: "Cybersecurity Professional",
    organization: "Taipei City Government",
    duration: "2022 - 2023",
    highlights: [
      "Led cybersecurity initiatives to protect critical government infrastructure",
      "Conducted vulnerability assessments and implemented security protocols",
      "Collaborated with cross-departmental teams to establish security best practices",
      "Developed and delivered security awareness training programs",
    ],
  },
  {
    title: "Information Technology Engineer",
    organization: "Elitegroup Computer Systems",
    duration: "2020 - 2022",
    highlights: [
      "Designed and maintained enterprise-level ERP and EDI systems",
      "Developed integration solutions between internal systems and external partners",
      "Optimized database performance and implemented data migration strategies",
      "Provided technical support and documentation for system operations",
    ],
  },
]

export function ExperienceSection() {
  return (
    <section id="experience" className="py-24 px-6 bg-secondary/30">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-12">
          Experience
        </h2>

        <div className="space-y-8">
          {experiences.map((experience, index) => (
            <div
              key={experience.title}
              className="relative pl-8 md:pl-12 pb-8 last:pb-0"
            >
              {/* Timeline Line */}
              {index !== experiences.length - 1 && (
                <div className="absolute left-[11px] md:left-[19px] top-10 bottom-0 w-px bg-border" />
              )}

              {/* Timeline Dot */}
              <div className="absolute left-0 md:left-2 top-0 w-6 h-6 rounded-full bg-primary flex items-center justify-center">
                <Briefcase className="h-3 w-3 text-primary-foreground" />
              </div>

              {/* Content */}
              <div className="bg-card rounded-xl border border-border p-6 ml-4 md:ml-6 hover:border-primary/50 transition-colors">
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-2 mb-4">
                  <div>
                    <h3 className="text-xl font-semibold text-foreground">
                      {experience.title}
                    </h3>
                    <p className="text-primary">{experience.organization}</p>
                  </div>
                  <span className="text-sm text-muted-foreground bg-secondary px-3 py-1 rounded-full w-fit">
                    {experience.duration}
                  </span>
                </div>

                <ul className="space-y-2">
                  {experience.highlights.map((highlight) => (
                    <li
                      key={highlight}
                      className="text-muted-foreground text-sm flex items-start gap-2"
                    >
                      <span className="text-primary mt-1.5">•</span>
                      {highlight}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
