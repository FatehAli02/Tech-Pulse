def build_email_html(articles):

    if not articles:
        return "<h3>No new tech news matching your keywords today.</h3>"

    sorted_articles = sorted(articles, key=lambda x: x.get('score', 0), reverse=True)

    pak_articles = [a for a in sorted_articles if a.get('region').lower() == 'pakistan']
    global_articles = [a for a in sorted_articles if a.get('region').lower() == 'global']

    html = """
    <html>
      <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
        <h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">
          🚀 Tech Pulse: Your Daily Digest
        </h2>
    """

    def build_section(title, article_list):
        section_html = f"<h3 style='color: #e74c3c; margin-top: 20px;'>{title}</h3>"
        if not article_list:
            section_html += "<p style='color: #7f8c8d; font-style: italic;'>No major updates in this sector today.</p>"
            return section_html
            
        for article in article_list:
            section_html += f"""
            <div style="margin-bottom: 20px; padding: 15px; background-color: #f9f9f9; border-left: 4px solid #3498db;">
                <h4 style="margin: 0 0 10px 0;">
                    <a href="{article['link']}" style="color: #2980b9; text-decoration: none;">{article['title']}</a>
                    <span style="font-size: 12px; color: #fff; background-color: #f39c12; padding: 3px 6px; border-radius: 3px; margin-left: 10px;">Score: {article['score']}</span>
                </h4>
                <p style="margin: 0; color: #555; font-size: 14px; line-height: 1.6; white-space: pre-line;">{article['body']}</p>
                <small style="color: #95a5a6; display: block; margin-top: 10px;">Source: {article['source']} | Tag: {article['region']}</small>
            </div>
            """
        return section_html

    html += build_section("🇵🇰 Pakistan Tech", pak_articles)
    html += build_section("🌍 Global Tech", global_articles)

    html += """
        <hr style="border: none; border-top: 1px solid #eee; margin-top: 30px;">
        <p style="font-size: 12px; color: #999; text-align: center;">Automated by Tech Pulse Bot 🤖</p>
      </body>
    </html>
    """
    
    return html