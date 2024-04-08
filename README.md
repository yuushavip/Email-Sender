# 批量寄信工具

使用 python 編寫的工具，可以自定義寄件名單、HTML信件模板，該專案也有附帶範例相關檔案提供參考，但寄件資訊相關設定不可以直接使用，請改成可以正常使用的設定。

`email_sender_config.ini`

提供設定基本的寄件資訊、SMTP相關設定。

`email_sender_info.yaml`

`settings`內的`email_tasks`可以自定義要寄信的項目，可以自定義多組設定，而每個設定會需要3個參數，`recipient_list` 是寄件名單、`email_subject` 是信件標題、`email_html` 是指定 HTML信件模板檔案。

---

# Email Sender

This is a tool written in Python that allows customization of the mailing list, HTML email template. The project also includes example files for reference. However, the mailing information and settings should not be used directly; please modify them to be properly usable.

`email_sender_config.ini`

Set up basic mailing information and SMTP settings.

`email_sender_info.yaml`

Within `settings`, `email_tasks` can be customized to define the email sending tasks. Multiple configurations can be set, and each configuration requires three parameters: `recipient_list` for the mailing list, `email_subject` for the email title, and `email_html` for the HTML email template.
