# SomTMS Marketing Site (somtms.com)

Static marketing website for SomTMS.
Login button directs to https://app.somtms.com

## Deploy to Firebase Hosting

1) Install Firebase CLI
```bash
npm i -g firebase-tools
firebase login
```

2) Initialize hosting in this folder
```bash
firebase init hosting
```

Recommended answers:
- Use existing Firebase project (marketing site project)
- Public directory: `.` (dot)
- Configure as single-page app: `No`

3) Deploy
```bash
firebase deploy --only hosting
```

## Custom domain
Firebase Console → Hosting → Add custom domain:
- somtms.com (and optional www.somtms.com)

App should be hosted separately at app.somtms.com.
