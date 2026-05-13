"use strict";

throw new Error("scanner fixture only; do not execute");

const child_process = require("child_process");

function runShell(userArg) {
  child_process.exec(`echo ${userArg}`);
  child_process.spawnSync("sh", ["-c", userArg]);
}

function buildFunction(userExpression) {
  const fn = new Function("input", userExpression);
  setTimeout("console.log(window.secret)", 10);
  return fn;
}

function readSecret(fs, name) {
  return fs.readFileSync(`/home/app/${name}`, "utf8");
}

module.exports = { runShell, buildFunction, readSecret };
