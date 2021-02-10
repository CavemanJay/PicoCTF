const { execSync } = require("child_process");

async function main() {
  const srcUrl = "https://jupiter.challenges.picoctf.org/problem/60786/";
  const src = execSync(`curl -sL ${srcUrl}`).toString();
  const passList = src
    .split("\n")
    .find((x) => x.includes("var "))
    .trim()
    .split(";")[0];

  const jsonString = passList
    .match(/\[.*\]/)[0]
    .replace(/'/g, '"')
    .replace(/\\/g, "");

  const parts = JSON.parse(jsonString);

  const flag = parts[8] + parts[9] + parts[1] + parts[0];

  console.log(flag);
}

(async function () {
  main();
})();
