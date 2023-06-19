from tabulate import tabulate
import urllib.parse
import time
import csv

categories = {
    "Video Player": {
        "Video Player Frameworks": [
            "video.js",
            "plyr",
            "jwplayer",
            "decrypted_player-v1",
        ],
        "Video File Extensions": ["mp4", "webm", "mp2t", "video", "tsfiles"],
    },
    "Advertisement": {
        "Ad Networks": [
            "adservice",
            "adfinity",
            "adfox",
            "fubotv.pxf",
            "googleads",
            "googlesyndication",
            "impactradius-go",
            "ntoftheusysianedt",
            "pogothere",
            "tubeskagos",
            "unmistisdune",
            "yadro",
            "yt3.ggpht",
            "adSense",
            "media.net",
            "taboola",
            "outbrain",
            "admob",
            "doubleclick",
            "googleadservices",
            "ssp-rtb.sape",
            "notix",
            "onlombreor",
            "rtmark",
            "regenerator-runtime",
            "escape-html",
            "gulsachpyrexia"
        ],
        "Ad Types": ["display-ads", "video-ads", "native-ads"],
        "Ad General": [
            "advertisement",
            "banner",
            "pop-up",
            "sponsored",
            "promoted",
        ],
    },
    "Images/GIFs": {
        "Image Asset": [
            "images",
            "img",
            "image",
            "jpg",
            "png",
            "gif",
            "jpeg",
            "svg",
        ],
    },
    "Content Delivery Networks (CDNs)": {
        "CDN Providers": [
            "maxcdn",
            "cdnjs",
            "cloudfront",
            "dudialgator",
            "iclickcdn",
            "spo-play",
            "taboola",
            "cdn",
            "cloudflare",
            "akamai",
            "fastly",
            "cloudfront",
            "cdn.taboola",
            "jsdelivr",
            "platform-cdn.sharethis",
        ],
        "Wordpress": ["wp-content", "wp-right", "wp-includes", "wp-rocket", "wp-content"],
        "Image CDN": [
            "vingartisticta",
        ],
        "CSS CDN": [],
        "JS CDN": [],
    },
    "Third-Party Plugins/Services": {
        "Payment Gateways": ["paypal", "stripe", "braintree"],
        "Other Plugins/Services": [
            "octet-stream",
            "binary",
        ],
        "Hosting": [
            "streamvid"
        ]
    },
    "Authentication": {
        "Login/Sign Up Services": ["oauth", "accounts.google", "facebook.com/login"],
        "User Management Systems": ["firebaseauth", "okta", "auth0"],
        "Auth General": ["login", "signin", "sign-in", "sign-up", "signup", "register"],
    },
    "Analytics": {
        "Analytics Platforms": [
            "google-analytics",
            "scorecardresearch",
            "googletagmanager",
            "yastatic",
            "acint",
            "webvisor",
        ],
        "Heatmap and User Tracking": ["hotjar", "crazy-egg", "mouseflow"],
        "Analytics General": [
            "analytics",
            "stats",
            "traffic",
            "visitors",
        ],
    },
    "Chat/Web Socket": {
        "Chat Services": ["youtube-live-chat", "twitch-chat", "discord", "chatango"],
        "Web Socket Connections": ["socket.io", "signalr", "pusher"],
    },
    "Frameworks and Libraries": {
        "JavaScript Libraries/Frameworks": [
            "bootstrap",
            "champaup",
            "escape-html",
            "fontawesome-webfont",
            "jquery",
            "lazyload",
            "md5",
            "pagead2",
            "practicalwhich",
            "psbar",
            "react",
            "react-dom",
            "slide",
            "star-rating",
            "angular",
            "regenerator-runtime",
            "redux-framework",
            "register-sw",
            "lazysizes",
            "element",
            "psbar",
            ""
        ],
        "Cookie Management Libraries": ["cookie.js", "vue-cookie"],
    },
    "Security": {
        "reCAPTCHA Integration": ["recaptcha", "gstatic"],
        "Content Security Policies": ["CSP"],
        # "SSL/TLS Certificates and HTTPS": [],
    },
    "Social Media Integration": {
        "Social Media Widgets": [
            "twitter",
            "instagram",
            "facebook",
            "twitch",
            "discord",
        ],
        "Social Sharing Plugins": ["addthis", "sharethis", "socialshare.js"],
        "Messaging Services": ["telegram", "whatsApp"],
    },
    "Content Management Systems (CMS)": {
        "CMS Platforms": ["wordPress", "drupal", "joomla"],
        "Headless CMS": ["contentful", "prismic", "strapi"],
        "General CMS": ["cms"],
    },
    "Bots": {
        "Search Engine Crawlers": [
            "Googlebot",
            "Baiduspider",
            "googlebot",
            "bingbot",
            "slurp",
            "yandex",
        ],
        "Web Scraping Bots": ["Scrapy", "BeautifulSoup"],
        "Monitoring and Testing Bots": ["Pingdom", "New Relic Synthetics"],
        "Chatbots and Virtual Assistants": [
            "dialogflow",
            "IBM-Watson",
            "Microsoft-Bot-Framework",
        ],
        "Data Aggregation Bots": ["Price-comparison bots", "News-aggregators"],
        "General Bot": [
            "bot",
            "crawler",
            "indexer",
            "spider",
        ],
    },
}


# Generate unique object IDs based on category and subcategory
def generate_object_id(category, subcategory):
    # Concatenate category and subcategory strings
    combined_string = category + subcategory
    # Hash the combined string
    object_id = hash(combined_string)
    # Ensure the object ID is positive
    object_id = abs(object_id)
    return object_id


# Prepare table data
table_data = []
headers = [
    "Object ID",
    "Object Name",
    "Category",
    "Subcategory",
    "Keywords",
    "Description",
    "Created",
    "Modified",
]

# Generate the "Created" timestamp (only once at the start)
created_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

# Iterate over the categories, subcategories, and keywords
for category, subcategories in categories.items():
    for subcategory, keywords in subcategories.items():
        # Generate the unique object ID
        object_id = generate_object_id(category, subcategory)
        # Generate the "Modified" timestamp (for each entry)
        modified_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        # Convert keywords list to string
        keywords_string = ", ".join(keywords)

        # Add the data to the table
        table_data.append(
            [
                object_id,
                "",
                category,
                subcategory,
                keywords_string,
                "",
                created_timestamp,
                modified_timestamp,
            ]
        )

# Generate the table
table = tabulate(table_data, headers, tablefmt="grid")
csv_data = []
csv_data.append(headers)
csv_data.extend(table_data)
# Write the table to a file
with open(
    "/home/debashishmajumdar/Documents/GitHub/intel-collection/outputs/network_call_object_table.csv",
    "w",
) as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
