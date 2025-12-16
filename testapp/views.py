from django.shortcuts import render

# Question class
class Questions:
    def __init__(self, que, a, b, c, d, correct, explanation):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct  # answer: 'a', 'b', 'c', 'd'
        self.explanation = explanation


def testpaper(request):
    questions = [
         Questions(
            "कोशिका झिल्ली का सर्वाधिक स्वीकृत मॉडल कौन-सा है?",
            "(a) यूनिट मेम्ब्रेन मॉडल",
            "(b) सैंडविच मॉडल",
            "(c) फ्लूड मोज़ेक मॉडल",
            "(d) माइसेलर मॉडल",
            "c",
            "सबसे स्वीकृत मॉडल Fluid Mosaic Model है।"
        ),

        Questions(
            "फ्लूड मोज़ेक मॉडल किसने दिया?",
            "(a) रॉबर्टसन",
            "(b) डैनियेली व डैवसन",
            "(c) सिंगर व निकोलसन",
            "(d) वाटसन व क्रिक",
            "c",
            "Singer और Nicolson ने Fluid Mosaic Model दिया।"
        ),

        Questions(
            "कोशिका झिल्ली मुख्यतः किससे बनी होती है?",
            "(a) केवल कार्बोहाइड्रेट",
            "(b) केवल प्रोटीन",
            "(c) लिपिड व प्रोटीन",
            "(d) लिपिड व कार्बोहाइड्रेट",
            "c",
            "Cell membrane मुख्यतः lipid और protein से बनी होती है।"
        ),

        Questions(
            "कोशिका झिल्ली की पारगम्यता कैसी होती है?",
            "(a) पूर्ण पारगम्य",
            "(b) अपारगम्य",
            "(c) चयनित पारगम्य",
            "(d) निर्जीव",
            "c",
            "Cell membrane selectively permeable होती है।"
        ),

        Questions(
            "निम्न में से कौन-सा निष्क्रिय परिवहन है?",
            "(a) Na⁺/K⁺ पम्प",
            "(b) एंडोसाइटोसिस",
            "(c) विसरण (Diffusion)",
            "(d) एक्सोसाइटोसिस",
            "c",
            "Diffusion passive transport का उदाहरण है।"
        ),

        Questions(
            "ध्रुवीय अणुओं के परिवहन हेतु आवश्यक है?",
            "(a) लिपिड द्विस्तर",
            "(b) कोलेस्ट्रॉल",
            "(c) वाहक प्रोटीन",
            "(d) राइबोसोम",
            "c",
            "Polar molecules carrier protein से transport होते हैं।"
        ),

        Questions(
            "सक्रिय परिवहन में किसकी आवश्यकता होती है?",
            "(a) ऑक्सीजन",
            "(b) एन्जाइम",
            "(c) ATP",
            "(d) जल",
            "c",
            "Active transport के लिए ATP आवश्यक होती है।"
        ),

        Questions(
            "सोडियम–पोटैशियम पम्प किसका उदाहरण है?",
            "(a) निष्क्रिय परिवहन",
            "(b) विसरण",
            "(c) परासरण",
            "(d) सक्रिय परिवहन",
            "d",
            "Na⁺/K⁺ pump active transport का उदाहरण है।"
        ),

        Questions(
            "Assertion (A): कोशिका झिल्ली चयनित पारगम्य होती है।\n"
            "Reason (R): कोशिका झिल्ली सभी पदार्थों को स्वतंत्र रूप से पार होने देती है।",
            "(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या करता है",
            "(b) A और R दोनों सही हैं, पर R सही व्याख्या नहीं करता",
            "(c) A सही है, R गलत है",
            "(d) A गलत है, R सही है",
            "c",
            "Cell membrane selectively permeable होती है, सभी पदार्थ freely नहीं जाते।"
        ),

        Questions(
            "Assertion (A): फ्लूड मोज़ेक मॉडल कोशिका झिल्ली का सबसे स्वीकृत मॉडल है।\n"
            "Reason (R): प्रोटीन फॉस्फोलिपिड द्विस्तर में पार्श्व गति करते हैं।",
            "(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या करता है",
            "(b) A और R दोनों सही हैं, पर R सही व्याख्या नहीं करता",
            "(c) A सही है, R गलत है",
            "(d) A गलत है, R सही है",
            "a",
            "Protein की lateral movement fluid mosaic nature दर्शाती है।"
        ),

        Questions(
            "Assertion (A): परासरण में जल का परिवहन होता है।\n"
            "Reason (R): जल उच्च जल सान्द्रता से निम्न जल सान्द्रता की ओर गति करता है।",
            "(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या करता है",
            "(b) A और R दोनों सही हैं, पर R सही व्याख्या नहीं करता",
            "(c) A सही है, R गलत है",
            "(d) A गलत है, R सही है",
            "a",
            "Osmosis में water higher concentration से lower की ओर जाता है।"
        ),

        Questions(
            "Assertion (A): सक्रिय परिवहन में ATP की आवश्यकता होती है।\n"
            "Reason (R): अणु सान्द्रता प्रवणता के विपरीत जाते हैं।",
            "(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या करता है",
            "(b) A और R दोनों सही हैं, पर R सही व्याख्या नहीं करता",
            "(c) A सही है, R गलत है",
            "(d) A गलत है, R सही है",
            "a",
            "Against concentration gradient movement के लिए ATP चाहिए।"
        ),
    ]

    from django.shortcuts import render

# Question class
class Questions:
    def __init__(self, que, a, b, c, d, correct, explanation):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct
        self.explanation = explanation


def testpaper(request):

    questions = [
        Questions(
            "कोशिका झिल्ली का सर्वाधिक स्वीकृत मॉडल कौन-सा है?",
            "(a) यूनिट मेम्ब्रेन मॉडल",
            "(b) सैंडविच मॉडल",
            "(c) फ्लूड मोज़ेक मॉडल",
            "(d) माइसेलर मॉडल",
            "c",
            "सबसे स्वीकृत मॉडल Fluid Mosaic Model है।"
        ),

        Questions(
            "फ्लूड मोज़ेक मॉडल किसने दिया?",
            "(a) रॉबर्टसन",
            "(b) डैनियेली व डैवसन",
            "(c) सिंगर व निकोलसन",
            "(d) वाटसन व क्रिक",
            "c",
            "Singer और Nicolson ने Fluid Mosaic Model दिया।"
        ),

        Questions(
            "कोशिका झिल्ली मुख्यतः किससे बनी होती है?",
            "(a) केवल कार्बोहाइड्रेट",
            "(b) केवल प्रोटीन",
            "(c) लिपिड व प्रोटीन",
            "(d) लिपिड व कार्बोहाइड्रेट",
            "c",
            "Cell membrane मुख्यतः lipid और protein से बनी होती है।"
        ),

        Questions(
            "कोशिका झिल्ली की पारगम्यता कैसी होती है?",
            "(a) पूर्ण पारगम्य",
            "(b) अपारगम्य",
            "(c) चयनित पारगम्य",
            "(d) निर्जीव",
            "c",
            "Cell membrane selectively permeable होती है।"
        ),

        Questions(
            "निम्न में से कौन-सा निष्क्रिय परिवहन है?",
            "(a) Na⁺/K⁺ पम्प",
            "(b) एंडोसाइटोसिस",
            "(c) विसरण (Diffusion)",
            "(d) एक्सोसाइटोसिस",
            "c",
            "Diffusion passive transport का उदाहरण है।"
        ),

        Questions(
            "ध्रुवीय अणुओं के परिवहन हेतु आवश्यक है?",
            "(a) लिपिड द्विस्तर",
            "(b) कोलेस्ट्रॉल",
            "(c) वाहक प्रोटीन",
            "(d) राइबोसोम",
            "c",
            "Polar molecules carrier protein से transport होते हैं।"
        ),

        Questions(
            "सक्रिय परिवहन में किसकी आवश्यकता होती है?",
            "(a) ऑक्सीजन",
            "(b) एन्जाइम",
            "(c) ATP",
            "(d) जल",
            "c",
            "Active transport के लिए ATP आवश्यक होती है।"
        ),

        Questions(
            "सोडियम–पोटैशियम पम्प किसका उदाहरण है?",
            "(a) निष्क्रिय परिवहन",
            "(b) विसरण",
            "(c) परासरण",
            "(d) सक्रिय परिवहन",
            "d",
            "Na⁺/K⁺ pump active transport का उदाहरण है।"
        ),

        Questions(
            "Assertion (A): कोशिका झिल्ली चयनित पारगम्य होती है।\n"
            "Reason (R): कोशिका झिल्ली सभी पदार्थों को स्वतंत्र रूप से पार होने देती है।",
            "(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या करता है",
            "(b) A और R दोनों सही हैं, पर R सही व्याख्या नहीं करता",
            "(c) A सही है, R गलत है",
            "(d) A गलत है, R सही है",
            "c",
            "Cell membrane selectively permeable होती है, सभी पदार्थ freely नहीं जाते।"
        ),

        Questions(
            "Assertion (A): फ्लूड मोज़ेक मॉडल कोशिका झिल्ली का सबसे स्वीकृत मॉडल है।\n"
            "Reason (R): प्रोटीन फॉस्फोलिपिड द्विस्तर में पार्श्व गति करते हैं।",
            "(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या करता है",
            "(b) A और R दोनों सही हैं, पर R सही व्याख्या नहीं करता",
            "(c) A सही है, R गलत है",
            "(d) A गलत है, R सही है",
            "a",
            "Protein की lateral movement fluid mosaic nature दर्शाती है।"
        ),

        Questions(
            "Assertion (A): परासरण में जल का परिवहन होता है।\n"
            "Reason (R): जल उच्च जल सान्द्रता से निम्न जल सान्द्रता की ओर गति करता है।",
            "(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या करता है",
            "(b) A और R दोनों सही हैं, पर R सही व्याख्या नहीं करता",
            "(c) A सही है, R गलत है",
            "(d) A गलत है, R सही है",
            "a",
            "Osmosis में water higher concentration से lower की ओर जाता है।"
        ),

        Questions(
            "Assertion (A): सक्रिय परिवहन में ATP की आवश्यकता होती है।\n"
            "Reason (R): अणु सान्द्रता प्रवणता के विपरीत जाते हैं।",
            "(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या करता है",
            "(b) A और R दोनों सही हैं, पर R सही व्याख्या नहीं करता",
            "(c) A सही है, R गलत है",
            "(d) A गलत है, R सही है",
            "a",
            "Against concentration gradient movement के लिए ATP चाहिए।"
        ),
    ]

    # =============== POST REQUEST (After Submit) ===============
    if request.method == "POST":

        score = 0
        detailed_result = []

        for i, q in enumerate(questions, 1):
            selected_option = request.POST.get(f'option{i}')

            if selected_option == q.correct:
                score += 1

            detailed_result.append({
                'question': q.que,
                'options': [q.a, q.b, q.c, q.d],
                'correct': q.correct,
                'selected': selected_option,
                'explanation': q.explanation
            })

        total = len(questions)
        percentage = round((score / total) * 100, 1)
        wrong_percentage = 100 - percentage

        # Send values to template
        context = {
            'score': score,
            'total': total,
            'percentage': percentage,
            'wrong_percentage': wrong_percentage,
            'result': detailed_result
        }

        return render(request, 'result.html', context)

    # =============== GET REQUEST (Show Questions) ===============
    return render(request, 'question.html', {'questions': questions})