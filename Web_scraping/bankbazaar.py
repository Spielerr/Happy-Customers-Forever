import scrapy

class Ver2(scrapy.Spider):
	name = "v2"
	page = 0
	start_urls = ["https://www.bankbazaar.com/reviews/indian-bank/all-products.html"]
	f = open("indian_bank.csv", "a+")
	
	def parse(self, response):
		last_page = int(response.css("div.pagination-review").css("span::text").extract()[0][response.css("div.pagination-review").css("span::text").extract()[0].rfind(' ')+1:])
		# reviews.extend(response.css("q.hotels-review-list-parts-ExpandableReview__reviewText--3oMkH::text").extract())
		reviews = response.css(".review-desc-more::text").extract()
		# review_titles.extend(response.css("div.hotels-review-list-parts-ReviewTitle__reviewTitle--2Fauz").css("a.hotels-review-list-parts-ReviewTitle__reviewTitleText--3QrTy").css("span::text").extract())
		# hotel_name = response.css("#HEADING::text").extract()
		# over_rating = response.css("div.ui_column  ").css("div.hotels-hotel-review-about-with-photos-Reviews__rating--2X_zZ").css("span.hotels-hotel-review-about-with-photos-Reviews__overallRating--vElGA::text")[0].extract()
		acc = (response.css("div.review-bank-title::text").extract())[1::2]
		title = response.css(".js-individual-title::text").extract()
		username = response.css(".js-author-name::text").extract()
		place = (response.css(".reviewer-profile::text").extract())[2::4]
		date = (response.css(".reviewer-profile::text").extract())[3::4]
		# for i in response.xpath("//div[contains(@class, 'hotels-hotel-review-about-with-photos-Reviews__subratingRow--2u0CJ')]").extract() :
		# 	ind_cats.append(int(i[200:202])/10)
		# ind_user_rat = []
		# for i in response.xpath("//div[contains(@class, 'hotels-review-list-parts-RatingLine__bubbles--1oCI4')]").extract() :
		# 	ind_user_rat.append(int(i[102:104])/10)
		# user_cont = []
		# for i in range(1,10,2):
		# 	user_cont.append(int((response.css(".social-member-MemberHeaderStats__stat_item--34E1r:nth-child(1) span , .social-member-MemberHeaderStats__hometown_stat_item--231iN+ .social-member-MemberHeaderStats__stat_item--34E1r span")[i].extract())[-8:-7]))
		# f.write("Account type,Review title,Review,Username,place,date\n")
		for i in range(0,len(reviews)):
			f.write(acc[i]);f.write(",")
			f.write(title[i]);f.write(",")
			f.write(reviews[i]);f.write(",")
			f.write(username[i]);f.write(",")
			f.write(place[i]);f.write("\n")
			f.write(date[i]);f.write("\n")
		d = {'rev_titles' : review_titles, 'rev' : reviews, 'over_rating' : over_rating, 'ind_user_rat' : ind_user_rat, 'categories' : ind_cats}
		yield d 
		
		while (Ver1.page <= (last_page-1)):
			Ver1.page += 1
			next_page = "https://www.bankbazaar.com/reviews/indian-bank/all-products.html" + "?reviewPageNumber=" + str(Ver1.page)
			yield response.follow(next_page, callback = self.parse)
