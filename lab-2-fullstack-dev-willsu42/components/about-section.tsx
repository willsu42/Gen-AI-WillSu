import { CheckCircle2 } from "lucide-react"

const strengths = [
  "Cross-functional communication",
  "Requirement analysis & documentation",
  "System thinking",
  "Data-driven decision making",
]

export function AboutSection() {
  return (
    <section id="about" className="py-24 px-6">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-12">
          About Me
        </h2>

        <div className="grid lg:grid-cols-2 gap-12">
          {/* Left Column - Description */}
          <div className="space-y-6 text-muted-foreground leading-relaxed">
            <p>
              I am a graduate student specializing in Information Management with a strong
              foundation in software development, data science, and system integration.
              My academic journey and professional experiences have equipped me with the
              skills to bridge the gap between technical implementation and business needs.
            </p>
            <p>
              Throughout my career, I have developed expertise in building scalable
              applications, conducting data analysis, and implementing secure systems.
              I am passionate about leveraging technology to solve complex problems and
              deliver user-centered solutions.
            </p>
            <p>
              I thrive in environments where I can collaborate with cross-functional
              teams, translate technical requirements into actionable plans, and
              contribute to projects that have meaningful impact.
            </p>
          </div>

          {/* Right Column - Key Strengths */}
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-foreground">Key Strengths</h3>
            <ul className="space-y-4">
              {strengths.map((strength) => (
                <li key={strength} className="flex items-center gap-3">
                  <CheckCircle2 className="h-5 w-5 text-primary flex-shrink-0" />
                  <span className="text-muted-foreground">{strength}</span>
                </li>
              ))}
            </ul>

            <div className="mt-8 p-6 bg-secondary/50 rounded-xl border border-border">
              <p className="text-sm text-muted-foreground">
                <span className="font-semibold text-foreground">Education Focus:</span>{" "}
                Information Management, Software Engineering, Data Science, and Cybersecurity.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
