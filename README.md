# Kitting Planner API caller

## Step 1: Configure "template_input.xlsx"
  
  ``stock`` : Mealkits on hand by recipes 

  ``lines`` : Line setup, copy paste from googlesheet. DO remember to give each line an ``id``

  ``recipeSettings``: Recipe Name, mk/crate and target speed, also give each recipe an ``id``

  ``teams``: Team roster
  

## Step 2: Run "covert_template_input.ipynb" 
-- Covert "template_input.xlsx" to JSON

## Step 3: Run "request_solution.py"
-- API POST

## Step 4: Run "DataInquisition.ipynb"
-- Parse the callback JSON to CSVs, sever as the "qucikAnalysis.pbix" datasource

## Step 5: Open Power BI file "qucikAnalysis.pbix" and refresh
-- visualize new kitting plan in Power BI 