# Deployment Instructions

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `cognitive-vidya`
3. Make it **PUBLIC** (required for Colab to access notebooks)
4. Do NOT initialize with README, .gitignore, or license
5. Click "Create repository"

## Step 2: Push Code to GitHub

Run these commands in your terminal from the `cognitive-vidya` directory:

```bash
git remote add origin https://github.com/Saidsp19/cognitive-vidya.git
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to repository Settings → Pages (left sidebar)
2. Under "Build and deployment":
   - Source: Select "GitHub Actions"
3. The workflow will automatically trigger on push

## Step 4: Wait for Deployment

1. Go to the "Actions" tab in your repository
2. You'll see the "Deploy to GitHub Pages" workflow running
3. Wait for it to complete (takes ~2-3 minutes)
4. Once successful, your site will be live at:
   
   **https://Saidsp19.github.io/cognitive-vidya/**

## Step 5: Test the Platform

1. Visit the live URL
2. Navigate to "Maximum Sum Subarray of Size K"
3. Click the "Open In Colab" badge
4. Verify Google Colab opens with the notebook
5. Run the cells to test the auto-grader

---

## Troubleshooting

If GitHub Actions fails:
- Check the Actions tab for error logs
- Ensure the repository is public
- Verify GitHub Pages is set to "GitHub Actions" source

If Colab cannot find the notebook:
- Ensure repository is public
- Check the notebook path matches the URL in the badge
- Wait a few minutes for GitHub to index the repository

---

## Architecture Summary

✅ **Frontend:** Docusaurus (React-based static site)
✅ **Hosting:** GitHub Pages (free)
✅ **CI/CD:** GitHub Actions (auto-deploy on push)
✅ **IDE:** Google Colab (zero-setup Python environment)
✅ **Content:** 5 foundational DSA problems with auto-graders

**Patterns covered:**
- Sliding Window (Fixed & Variable)
- HashMap
- Stack
- Binary Search

**Next steps to scale:**
- Add more problems per pattern
- Implement difficulty filters
- Add video explanations
- Create progress tracking
