(() => {
  const links = document.querySelectorAll(".resume-download[data-preferred]");

  links.forEach(async (link) => {
    const preferred = link.dataset.preferred;
    if (!preferred) return;

    try {
      const response = await fetch(preferred, { method: "HEAD", cache: "no-store" });
      if (!response.ok) return;

      link.href = preferred;

      const readyLabel = link.dataset.readyLabel;
      if (readyLabel) {
        const suffix = link.querySelector("span")?.outerHTML || "";
        link.innerHTML = suffix ? `${readyLabel} ${suffix}` : readyLabel;
      }
    } catch {
      // Keep the existing fallback link when a localized CV is not available yet.
    }
  });
})();