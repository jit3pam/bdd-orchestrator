const report = require("multiple-cucumber-html-reporter");

report.generate({
  jsonDir: "reports/cucumber",
  reportPath: "reports/html",
  metadata: {
    browser: {
      name: "Chrome",
      version: "Latest",
    },
    device: "Local machine",
    platform: {
      name: "Windows / Linux",
    },
  },
  customData: {
    title: "Run info",
    data: [
      { label: "Project", value: "bdd-orchestrator" },
      { label: "Execution", value: "Local / CI" },
    ],
  },
});
