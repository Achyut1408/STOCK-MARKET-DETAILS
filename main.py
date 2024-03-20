from fastapi import FastAPI, Query
from yfinance import Ticker
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class CompanyDetails(BaseModel):
    name: str | None = None
    symbol: str | None = None
    sector: str | None = None
    country: str | None = None
    website: str | None = None
    major_holders: dict | None = None
    institutional_holders: dict | None = None

@app.get("/", response_class=HTMLResponse)
async def get_index():
    return HTMLResponse(content=open("index.html", "r").read(), status_code=200)

@app.get("/company-details")
async def get_company_details(symbol: str = Query(..., help="Company symbol", example="AAPL")):
    try:
        company = Ticker(symbol)
        company_info = company.info
        company_details = CompanyDetails(
            name=company_info.get("shortName"),
            symbol=company_info.get("symbol"),
            sector=company_info.get("sector"),
            country=company_info.get("country"),
            website=company_info.get("website"),
            major_holders=company.major_holders.to_dict(),
            institutional_holders=company.institutional_holders.to_dict(),
        )
        return company_details
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.mount("/", StaticFiles(directory=".", html=True), name="static")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
