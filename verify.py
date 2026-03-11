from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Emulate reduced motion
        browser = p.chromium.launch()
        context_reduced = browser.new_context(reduced_motion="reduce")
        page_reduced = context_reduced.new_page()

        errors = []
        page_reduced.on("pageerror", lambda err: errors.append(err.message))
        page_reduced.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

        # Abort font loading
        page_reduced.route("**/*.woff", lambda route: route.abort())
        page_reduced.route("**/*.ttf", lambda route: route.abort())
        page_reduced.route("**/fonts.googleapis.com/**", lambda route: route.abort())

        print("Navigating to page with reduced motion...")
        page_reduced.goto("http://localhost:8000/index.html", wait_until="commit")

        # Check if the elements have the active class immediately
        lines = page_reduced.locator(".content > h1")
        lines.wait_for(state="attached")
        print("Page loaded. Checking for active class...")

        # We can just check the first h1 to see if it has 'active' but not 'scramble-line'
        h1_class = page_reduced.eval_on_selector("h1", "el => el.className")
        print(f"H1 classes (reduced motion): {h1_class}")
        assert "active" in h1_class
        assert "scramble-line" not in h1_class

        print(f"Console/Page errors: {errors}")
        assert len(errors) == 0

        # Now check with normal motion
        context_normal = browser.new_context(reduced_motion="no-preference")
        page_normal = context_normal.new_page()
        page_normal.route("**/*.woff", lambda route: route.abort())
        page_normal.route("**/*.ttf", lambda route: route.abort())
        page_normal.route("**/fonts.googleapis.com/**", lambda route: route.abort())

        print("Navigating to page with normal motion...")
        page_normal.goto("http://localhost:8000/index.html", wait_until="commit")

        # wait a bit for js to run
        page_normal.wait_for_timeout(100)
        h1_class_normal = page_normal.eval_on_selector("h1", "el => el.className")
        print(f"H1 classes (normal motion): {h1_class_normal}")
        assert "scramble-line" in h1_class_normal

        browser.close()
        print("Verification passed successfully.")

if __name__ == "__main__":
    verify()
