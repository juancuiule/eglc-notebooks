const pipInstall = Deno.run({
  cmd: ["python", "-m", "pip", "install", "-r", "requirements.txt"],
});

await pipInstall.status();

const pyRun = Deno.run({
  cmd: ['python', './pp-change-blindness.py'],
});

await pyRun.status();
