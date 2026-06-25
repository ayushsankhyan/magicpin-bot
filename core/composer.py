# core/composer.py

class Composer:

    def compose(self, facts, strategy, memory=None):

        trigger = facts.get("trigger_kind")

        merchant = (
            facts.get("merchant_name")
            or "Your business"
        )

        city = (
            facts.get("city")
            or "your area"
        )
        locality = (
            facts.get("locality")
            or city
        )

        category = facts.get("category_slug", "business")

        views = facts.get("views", 0)

        leads = facts.get("leads", 0)

        ctr = facts.get("ctr", 0)

        offers = facts.get("offers", [])

        reviews = facts.get("review_themes", [])

        if offers:

            offer = offers[0]

        elif category == "dentists":

            offer = "your dental services"

        elif category == "salons":

            offer = "your beauty services"

        elif category == "restaurants":

            offer = "your popular menu items"

        elif category == "gyms":

            offer = "your membership plans"

        elif category == "pharmacies":

            offer = "your healthcare products"

        else:

            offer = "your services"

        last_conversation = facts.get("last_conversation", "")

        research_topic = facts.get("research_topic")

        # ==========================
        # Research
        # ==========================

        if trigger == "research_digest":

            interest = ""

            text = last_conversation.lower()

            if "whitening" in text:

                interest = "whitening"

            elif "aligner" in text:

                interest = "aligners"

            elif text:

                interest = "patient acquisition"

            # =====================================
            # Merchant previously discussed a topic
            # =====================================

            if interest:

                return (

                    f"You recently asked about "
                    f"{interest}.\n\n"

                    f"A new research update could help "
                    f"{merchant} answer patient questions "
                    f"more confidently and improve "
                    f"consultation quality.\n\n"

                    f"Would you like the "
                    f"2-minute summary?"
                )

            # =====================================
            # Dentist
            # =====================================

            if category == "dentists":

                return (

                    f"A new dental research update "
                    f"is available for {merchant}.\n\n"

                    f"It may help answer patient "
                    f"questions more confidently during "
                    f"consultations.\n\n"

                    f"Would you like the "
                    f"2-minute summary?"
                )

            # =====================================
            # Salon
            # =====================================

            if category == "salons":

                return (

                    f"A new beauty industry trend "
                    f"report is available for "
                    f"{merchant}.\n\n"

                    f"It may help you recommend "
                    f"popular services and improve "
                    f"customer conversations.\n\n"

                    f"Would you like the summary?"
                )

            # =====================================
            # Gym
            # =====================================

            if category == "gyms":

                return (

                    f"A new fitness industry insight "
                    f"is available for {merchant}.\n\n"

                    f"It may help improve member "
                    f"engagement and encourage "
                    f"new sign-ups.\n\n"

                    f"Would you like the summary?"
                )

            # =====================================
            # Pharmacy
            # =====================================

            if category == "pharmacies":

                return (

                    f"A new pharmacy industry update "
                    f"is available for {merchant}.\n\n"

                    f"It may help answer customer "
                    f"questions and prepare for "
                    f"changing demand.\n\n"

                    f"Would you like the summary?"
                )

            # =====================================
            # Restaurant
            # =====================================

            if category == "restaurants":

                return (

                    f"A new restaurant industry trend "
                    f"report is available for "
                    f"{merchant}.\n\n"

                    f"It may help identify customer "
                    f"preferences and improve menu "
                    f"promotions.\n\n"

                    f"Would you like the summary?"
                )

            # =====================================
            # Generic Fallback
            # =====================================

            return (

                f"A new industry research update "
                f"is available for {merchant}.\n\n"

                f"It may help support better "
                f"business decisions.\n\n"

                f"Would you like the summary?"
            )

        # ==========================
        # Performance Dip
        # ==========================

        if trigger == "perf_dip":

            ctr_pct = round(
                ctr * 100,
                1
            )

            return (

                f"{merchant} received "
                f"{views} profile views, "
                f"but only {ctr_pct}% of visitors "
                f"are clicking through.\n\n"

                f"Your active offer "
                f"'{offer}' may not be getting "
                f"enough visibility around "
                f"{locality}, which could be "
                f"limiting new customer enquiries.\n\n"

                f"Would you like "
                f"3 ideas to improve conversions?"
            )

        # ==========================
        # Performance Spike
        # ==========================

        if trigger == "perf_spike":

            return (

                f"{merchant} is attracting "
                f"stronger engagement than usual, "
                f"with {views} profile views and "
                f"{leads} recent leads.\n\n"

                f"Your active offer "
                f"'{offer}' could help convert "
                f"this increased interest into "
                f"more customers across {city}.\n\n"

                f"Would you like "
                f"3 ideas to build on this momentum?"
            )

        # ==========================
        # Renewal
        # ==========================

        if trigger == "renewal_due":

            days = facts.get("days_remaining")

            amount = facts.get("renewal_amount")

            plan = facts.get("plan")

            if days:

                renewal_text = (
                    f"Your {plan} plan renews "
                    f"in {days} days"
                )

            else:

                renewal_text = (
                    "Your subscription is "
                    "approaching renewal"
                )

            if amount:

                renewal_text += (f" (₹{amount})")

            return (

                f"{merchant} generated "
                f"{views} views and "
                f"{leads} leads recently.\n\n"

                f"{renewal_text}.\n\n"

                f"Would you like a "
                f"performance summary?"
            )

        # ==========================
        # Competitor
        # ==========================

        if trigger == "competitor_opened":

            return (

                f"A new competitor appears to be "
                f"targeting customers near "
                f"{locality}.\n\n"

                f"{merchant} already attracts "
                f"{views} profile views. Highlighting "
                f"your active offer '{offer}' could help "
                f"maintain visibility and attract more "
                f"customers.\n\n"

                f"Would you like "
                f"3 ideas to stay ahead?"
            )

        # ==========================
        # Reviews
        # ==========================

        if trigger == "review_theme_emerged":

            review = None

            if reviews:
                review = reviews[0]

            theme = facts.get("review_theme")

            if not theme and review:
                theme = review.get("theme")

            if not theme:

                if category == "salons":
                    theme = "service quality"

                elif category == "restaurants":
                    theme = "food experience"

                elif category == "pharmacies":
                    theme = "staff support"

                elif category == "gyms":
                    theme = "member experience"

                else:
                    theme = "customer experience"

            occurrences = (
                review.get("occurrences_30d")
                if review
                else None
            )

            quote = (
                review.get("common_quote")
                if review
                else None
            )

            sentiment = (
                review.get("sentiment")
                if review
                else None
            )

            if occurrences:

                intro = (
                    f"{occurrences} recent reviews mention "
                    f"'{theme}'."
                )

            else:

                intro = (
                    f"Recent customer reviews mention "
                    f"'{theme}'."
                )

            if sentiment == "neg":

                impact = (
                    "Addressing this trend could improve "
                    "ratings, customer trust, and future enquiries."
                )

            else:

                impact = (
                    "Building on this positive feedback could "
                    "help strengthen your reputation."
                )

            message = (

                f"{intro}\n\n"

                f"{impact}"
            )

            if quote:

                message += (

                    f"\n\nExample customer feedback:\n"
                    f"\"{quote}\""
                )

            message += (

                "\n\nWould you like "
                "3 recommendations?"
            )

            return message

        # ==========================
        # Milestone
        # ==========================

        if trigger == "milestone_reached":

            return (

                f"Congratulations.\n\n"

                f"{merchant} has reached "
                f"{views} profile views and "
                f"generated {leads} leads.\n\n"

                f"This is a strong opportunity "
                f"to build on recent momentum. "
                f"Your active offer '{offer}' "
                f"could help convert this visibility "
                f"into even more enquiries.\n\n"

                f"Would you like "
                f"3 ideas to accelerate growth?"
            )

        # ==========================
        # Recall
        # ==========================

        if trigger == "recall_due":

            service = (facts.get("service_due") or "scheduled service")

            return (

                f"A customer is due for "
                f"{service} at {merchant}.\n\n"

                f"Timely follow-ups often "
                f"increase repeat visits.\n\n"

                f"Would you like a reminder draft?"
            )

        # ==========================
        # Festival
        # ==========================

        if trigger == "festival_upcoming":

            festival = (facts.get("festival_name") or "the upcoming festival")

            return (

                f"{festival} may increase "
                f"demand around {city}.\n\n"

                f"Your offer '{offer}' could "
                f"help attract new customers.\n\n"

                f"Would you like campaign ideas?"
            )

        # ==========================
        # Regulation Change
        # ==========================

        if trigger == "regulation_change":

            deadline = facts.get(
                "trigger_payload",
                {}
            ).get(
                "deadline_iso",
                ""
            )

            return (

                f"A new compliance update may "
                f"affect {merchant}.\n\n"

                f"Required action should be "
                f"completed before {deadline}.\n\n"

                f"Would you like a quick summary?"
            )

        # ==========================
        # Wedding Package Followup
        # ==========================

        if trigger == "wedding_package_followup":

            days = facts.get(
                "trigger_payload",
                {}
            ).get(
                "days_to_wedding"
            )

            return (

                f"A bridal customer is "
                f"{days} days away from their "
                f"wedding.\n\n"

                f"This could be a good time "
                f"to discuss preparation packages.\n\n"

                f"Would you like a follow-up draft?"
            )

        # ==========================
        # IPL Match Today
        # ==========================

        if trigger == "ipl_match_today":

            payload = facts.get(
                "trigger_payload",
                {}
            )

            match = payload.get(
                "match",
                "today's match"
            )

            venue = payload.get(
                "venue",
                city
            )

            return (

                f"{match} is scheduled today "
                f"at {venue}.\n\n"

                f"Your offer '{offer}' could "
                f"help attract match-day orders.\n\n"

                f"Would you like a promotion idea?"
            )

        # ==========================
        # Seasonal Performance Dip
        # ==========================

        if trigger == "seasonal_perf_dip":

            return (

                f"Recent visibility appears lower "
                f"than usual, but current patterns "
                f"look seasonal.\n\n"

                f"This may be a good time to test "
                f"new acquisition ideas.\n\n"

                f"Would you like suggestions?"
            )

        # ==========================
        # Supply Alert
        # ==========================

        if trigger == "supply_alert":

            molecule = facts.get(
                "trigger_payload",
                {}
            ).get(
                "molecule",
                "a product"
            )

            return (

                f"A supply alert has been issued "
                f"for {molecule}.\n\n"

                f"Reviewing inventory and customer "
                f"communication may help avoid disruption.\n\n"

                f"Would you like a summary?"
            )

        # ==========================
        # Category Seasonal
        # ==========================

        if trigger == "category_seasonal":

            trends = facts.get(
                "trigger_payload",
                {}
            ).get(
                "trends",
                []
            )

            trend = (
                trends[0]
                if trends
                else "seasonal demand"
            )

            return (

                f"Current seasonal trends show "
                f"{trend} in {city}.\n\n"

                f"Your offer '{offer}' may help "
                f"capture this demand.\n\n"

                f"Would you like recommendations?"
            )

        # ==========================
        # GBP Unverified
        # ==========================

        if trigger == "gbp_unverified":

            return (

                f"Your business profile may still "
                f"require verification.\n\n"

                f"Verified listings can improve "
                f"visibility significantly.\n\n"

                f"Would you like verification steps?"
            )

        # ==========================
        # CDE Opportunity
        # ==========================

        if trigger == "cde_opportunity":

            credits = facts.get(
                "trigger_payload",
                {}
            ).get(
                "credits",
                0
            )

            return (

                f"A continuing education opportunity "
                f"worth {credits} credits is available.\n\n"

                f"It may be relevant for dental professionals.\n\n"

                f"Would you like details?"
            )

        # ==========================
        # Engagement
        # ==========================

        if trigger == "trial_followup":

            return (

                f"Someone recently showed interest "
                f"in {offer}.\n\n"

                f"A quick follow-up often improves "
                f"conversion rates.\n\n"

                f"Would you like a follow-up draft?"
            )

        if trigger == "curious_ask_due":

            return (

                f"You recently explored growth ideas "
                f"for {merchant}.\n\n"

                f"There may be opportunities around "
                f"{locality} worth testing.\n\n"

                f"Would you like suggestions?"
            )

        if trigger == "dormant_with_vera":

            return (

                f"It's been a while since we discussed "
                f"growth opportunities for {merchant}.\n\n"

                f"Market conditions may have changed "
                f"in {city}.\n\n"

                f"Would you like an updated action plan?"
            )

        if trigger == "active_planning_intent":

            return (

                f"You appear to be actively planning "
                f"business growth.\n\n"

                f"{merchant} already receives "
                f"{views} profile views.\n\n"

                f"Would you like next-step recommendations?"
            )

        # ==========================
        # Refill
        # ==========================

        if trigger == "chronic_refill_due":

            if category == "pharmacies":

                return (

                    f"Several customers may soon "
                    f"require medication refills.\n\n"

                    f"Timely refill reminders can help "
                    f"improve continuity of care.\n\n"

                    f"Would you like a refill outreach plan?"
                )

            elif category == "gyms":

                return (

                    f"Some members may be approaching "
                    f"their renewal cycle.\n\n"

                    f"A proactive reminder can help "
                    f"improve retention.\n\n"

                    f"Would you like a member re-engagement campaign?"
                )

            elif category == "salons":

                return (

                    f"Past customers may be due for "
                    f"their next beauty service.\n\n"

                    f"Follow-up reminders often increase "
                    f"repeat bookings.\n\n"

                    f"Would you like a booking reminder draft?"
                )

            else:

                return (

                    f"Some customers may soon need "
                    f"repeat purchases or follow-ups.\n\n"

                    f"Proactive outreach can improve "
                    f"retention and repeat business.\n\n"

                    f"Would you like campaign suggestions?"
                )

        # ==========================
        # Appointment
        # ==========================

        if trigger == "appointment_tomorrow":

            return (

                f"{merchant} has upcoming "
                f"appointments scheduled.\n\n"

                f"Reminder messages can reduce "
                f"missed visits.\n\n"

                f"Would you like templates?"
            )

        # ==========================
        # Winback
        # ==========================

        if trigger == "customer_lapsed_soft":

            return (

                f"Some customers have not visited "
                f"{merchant} recently.\n\n"

                f"A gentle reminder or limited-time "
                f"offer could encourage another visit.\n\n"

                f"Would you like a win-back campaign?"
            )

        if trigger == "customer_lapsed_hard":

            return (

                f"Several customers appear inactive "
                f"for an extended period at "
                f"{merchant}.\n\n"

                f"A stronger re-engagement offer may "
                f"help recover lost customers.\n\n"

                f"Would you like campaign ideas?"
            )

        if trigger == "winback_eligible":

            return (

                f"Past customers of {merchant} may be "
                f"ready to return with the right offer.\n\n"

                f"Your '{offer}' promotion could help "
                f"restart engagement.\n\n"

                f"Would you like a win-back strategy?"
            )