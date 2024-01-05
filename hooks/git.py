from mkdocs import plugins


@plugins.event_priority(100)
def on_page_markdown(markdown, page, config, files):
    markdown += "\n\nLast updated: {{ git.date.strftime('%b %d, %Y at %I:%M %p') }}"
    return markdown
