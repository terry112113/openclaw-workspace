$skillDirs = @(
    'academic-deep-research','academic-writing','accountant','add-analytics','agent-browser',
    'ai-web-automation','analytics-tracking-2','angular','api-designer','api-dev','apollo-api',
    'apple-health-skill','audio-cog','banshee-s-last-cry','branding','brave-search',
    'browser-automation','browser-use','business','business-administration','business-writing',
    'cicd-pipeline','clipboard','content-automation','data-analyst-pro','deepresearchwork',
    'desktop-control','devops','document-processor','douyin-downloader','ecommerce','excel-xlsx',
    'fitness','git','gitflow','health','healthy-eating','image-process','image-read',
    'japanese-translation-and-tutor','jobber','knowledge-graph','lambda-lang','langchain',
    'learning','linear-api','marketing-mode','mbb-strategist','memory-management','music-cog',
    'pdf-toolkit-pro','personal-productivity','projects','quant-analyst','rag','react-expert',
    'screenshot','self-improving','senior-data-engineer','seo','seo-content-writer','seo-optimizer',
    'sheet-cog','skill-creator','slides-cog','social-media-scheduler','stock-analysis','superdesign',
    'system-info','tushare-finance','typescript-pro','ui-ux-pro-max','video-cog','video-generation',
    'video-tool-watermark-remove','watermark','wbs-planner','web','web-search'
)

$base = 'C:\Users\TL\.openclaw\workspace-main\skills'
foreach ($d in $skillDirs) {
    $path = Join-Path $base $d 'SKILL.md'
    $content = if (Test-Path $path) { Get-Content $path -Raw } else { 'NO SKILL.MD' }
    Write-Host "=== $d ==="
    Write-Host $content
    Write-Host ''
}
