package scraper

type News struct {
	Id          string   `json:"id"`
	Date        string   `json:"date"`
	Title       string   `json:"title"`
	Description string   `json:"description"`
	Tags        []string `json:"tags"`
	Link        string   `json:"link"`
}

type Scraper interface {
	FetchNewsFromWebsite() []News
}

type SeScraper struct {
	website string
}

func New(website string) Scraper {
	return SeScraper{website: website}
}

func (SeScraper) FetchNewsFromWebsite() []News {
	return []News{
		{
			Id:          "12431",
			Date:        "07.09.2019 16:30",
			Title:       "Agnieszka Kaczorowska i Maciej Pela świętują PIERWSZĄ ROCZNICĘ ŚLUBU na wycieczce z córeczką: \"Emi, nasza dzielna podróżniczka\"",
			Description: "Pamiętacie obszerną relację z ich bajkowego ślubu w Toskanii? Po roku wrócili do Włoch.",
			Tags:        []string{"Penn", "Teller"},
			Link:        "https://www.pudelek.pl/artykul/150717/agnieszka_kaczorowska_i_maciej_pela_swietuja_pierwsza_rocznice_slubu_na_wycieczce_z_coreczka_emi_nasza_dzielna_podrozniczka/",
		},
	}
}
