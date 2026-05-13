selection = '''
    Please list sentences that most relevant to the claim based on the context provided in the evidence and your own knowledge.

    Claim: Barack Obama is dead.
    Evidence: 1. May 2, 2011 ... President Barack Obama · Vice President Joe Biden · First Lady Michelle ... President Obama on Death of Osama bin Laden. The Obama White House. 2. Obama's mother was survived by her Kansas-born mother, Madelyn Dunham, until her death on November 2, 2008, two days before his election to the presidency. 3. Jul 25, 2023 ... Former United States President Barack Obama's personal chef has been found dead in a lake near the Obamas' family home, in the resort ... 4. Barack Obama, the 44th president, recently died in a house fire due to Michelle Obama cooking March 31, 2023. The stove in the house leaked into a fire which ... 5. Barack Obama dead on April 1, 2023.
    >>>>>>
    Output: 4. Barack Obama, the 44th president, recently died in a house fire due to Michelle Obama cooking March 31, 2023. The stove in the house leaked into a fire which ... 5. Barack Obama dead on April 1, 2023.
    ------
    Claim: {0}
    Evidence: {1}
    >>>>>>
'''

correlation_degree = '''
    Please judge the correlation degree between each claim and its corresponding evidence from the options provided: a) The evidence definitely supports the claim; b) The evidence definitely contradicts the claim; c) The evidence indirectly supports the claim; d) The evidence indirectly contradicts the claim; e) The evidence partially supports the claim; f) The evidence partially contradicts the claim; g) The evidence has no relation with the claim. You can treat the claim as the context of the evidence when there are unclear references occur in evidence.

    Claim: Barack Obama is dead.
    Evidence: @BarackObama has just passed. The President is dead. A sad 4th of July, indeed. President Barack Obama is dead," came the first tweet.
    >>>>>>
    Correlation: The evidence definitely supports the claim. 
    ------
    Claim: Barack Obama is dead.
    Evidence: A personal chef for Barack Obama drowned Sunday in a paddle board accident near the former president's home in Martha's Vineyard.
    >>>>>>
    Correlation: The evidence has no relation with the claim. 
    ------
    Claim: CDC Says Vaccinated Americans Have Higher Risk of Infection than Unvaccinated.
    Evidence: some people are more likely than others to get very sick if they get COVID-19 or who have received vaccines.
    >>>>>>
    Correlation: The evidence partially supports the claim. 
    ------
    Claim: CDC Says Vaccinated Americans Have Higher Risk of Infection than Unvaccinated.
    Evidence: infected with Delta be less infectious than infected unvaccinated people.
    >>>>>>
    Correlation: The evidence definitely contradicts the claim. 
    ------
    Claim: Due Date was shot in space.
    Evidence: The film was shot in Las Cruces , New Mexico , Atlanta , Georgia , and Tuscaloosa , Alabama .
    >>>>>>
    Correlation:  The evidence indirectly contradicts the claim. 
    ------
    Claim: Mass fish death in Malaysia caused by algal bloom, not Fukushima wastewater.
    Evidence: Researches show that neurotoxins produced by harmful wastewater in Malaysia may cause massive fish kills.
    >>>>>>
    Correlation: The evidence partially contradicts the claim.
    ------ 
    Claim: Alice Cooper was born on February 4th, 1948.
    Evidence: Vincent Damon Furnier was born on February 4, 1948, in Detroit, Michigan, the son of Ether Moroni Furnier (1924-1987) and his wife Ella Mae.
    >>>>>>
    Correlation: The evidence indirectly supports the claim. 
    ------
    Claim: {0}
    Evidence: {1}
    >>>>>>
'''

verification_w_correlation_split = '''
    Please verify the truth of the following claim with label 'True', 'False', or 'Uncertain' based on the evidence and correlation provided, and briefly explain why you get this conclusion. Try not to label 'Uncertain' when not all correlations are 'The evidence has no relation with the claim':

    Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
    Evidence & Correlation: Evidence 1: Fox television series New Amsterdam. As a result of filming that series' pilot, Coster-Waldau obtained his Screen Actors Guild card. He later recalled... & Correlation 1: The evidence definitely supports the claim.\n Evidence 2: Oct 16, 2020 ... 2009 Fox television film Virtuality , originally intended as a pilot. & Correlation 2: The evidence has no relation with the claim.\n
    >>>>>>
    Output: Label: True.     Explanation: Based on the evidence provided, it is evident that Nikolaj Coster-Waldau worked with the Fox Broadcasting Company. The first piece of evidence mentions his involvement in the Fox television series "New Amsterdam," which directly supports the claim. Additionally, obtaining his Screen Actors Guild card as a result of filming for this series further confirms his collaboration with Fox. Therefore, considering this strong correlation between the evidence and claim, it can be concluded that Nikolaj Coster-Waldau did indeed work with the Fox Broadcasting Company.
    ------ 
    Claim: The Cry of the Owl is based on a book by a Hungarian novelist.
    Evidence & Correlation: Evidence 1: The Cry of the Owl is a 2009 thriller film based on Patricia Highsmith 's book of the same name. & Correlation 1: The evidence definitely contradicts the claim.\n Evidence 2: Patricia Highsmith ( January 19 , 1921 -- February 4 , 1995 ) was an American novelist and short story writer , known for her psychological thrillers , which led to more than two dozen film adaptations. & Correlation 2: The evidence has no relation with the claim.\n
    >>>>>>
    Output: Label: False.     Explanation: The claim states that "The Cry of the Owl" is based on a book by a Hungarian novelist. However, the evidence provided contradicts this claim. Evidence 1 clearly states that "The Cry of the Owl" is based on Patricia Highsmith's book, and it specifies that this correlation definitely contradicts the claim since Patricia Highsmith was not Hungarian. Furthermore, Evidence 2 provides additional context about Patricia Highsmith being an American novelist and short story writer rather than Hungarian. Therefore, since both pieces of evidence indicate that Patricia Highsmith was American and there is no mention or implication of her being Hungarian or any connection to Hungary in relation to "The Cry of the Owl," we can conclude with certainty that the original claim is false.
    ------
    Claim: {0}
    Evidence & Correlation: {1}
    >>>>>>
'''

verification_wo_correlation_split = '''
    Please verify the truth of the following claim with label 'True', 'False', or 'Uncertain' based on the evidence provided, and briefly explain why you get this conclusion. Try not to label 'Uncertain' if evidence provided:


    Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
    Evidence: Evidence 1: Fox television series New Amsterdam. As a result of filming that series' pilot, Coster-Waldau obtained his Screen Actors Guild card. He later recalled...  \n Evidence 2: Oct 16, 2020 ... 2009 Fox television film Virtuality , originally intended as a pilot. \n
    >>>>>>
    Output: Label: True.     Explanation: Based on the evidence provided, it is true that Nikolaj Coster-Waldau worked with the Fox Broadcasting Company. The first piece of evidence mentions his involvement in the Fox television series "New Amsterdam," and how he obtained his Screen Actors Guild card as a result of filming its pilot. Additionally, there is mention of him working on a 2009 Fox television film called "Virtuality," which was originally intended as a pilot. Therefore, based on this evidence, it can be concluded that Nikolaj Coster-Waldau has indeed worked with the Fox Broadcasting Company.
    ------ 
    Claim: The Cry of the Owl is based on a book by a Hungarian novelist.
    Evidence: Evidence 1: The Cry of the Owl is a 2009 thriller film based on Patricia Highsmith 's book of the same name . \n Evidence 2: Patricia Highsmith ( January 19 , 1921 -- February 4 , 1995 ) was an American novelist and short story writer , known for her psychological thrillers , which led to more than two dozen film adaptations . \n
    >>>>>>
    Output: Label: False.     Explanation: The claim that "The Cry of the Owl" is based on a book by a Hungarian novelist is false. The evidence provided clearly states that "The Cry of the Owl" is based on Patricia Highsmith's book of the same name. Patricia Highsmith was an American novelist and short story writer, known for her psychological thrillers, which have led to numerous film adaptations. Therefore, it can be concluded from this evidence that the source material for "The Cry of the Owl" comes from an American author, not a Hungarian one.
    ------ 
    Claim: {0}
    Evidence: {1}
    >>>>>>
'''

verification_in_chain = '''
    "Please verify the label ('True', 'False', or 'Uncertain') of the claim with a briefly explanation on why you get this conclusion based on the evidence and corresponding correlation degree between each piece of evidence and claim provided. Try not to label 'Uncertain' if evidence provided.:

    Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
    Evidence & Correlation: Evidence 1: Fox television series New Amsterdam. As a result of filming that series' pilot, Coster-Waldau obtained his Screen Actors Guild card. He later recalled... & Correlation 1: The evidence definitely supports the claim.\n Evidence 2: Oct 16, 2020 ... 2009 Fox television film Virtuality , originally intended as a pilot. & Correlation 2: The evidence has no relation with the claim.\n
    >>>>>>
    Output: Label: True.     Explanation: Based on the evidence provided, it is evident that Nikolaj Coster-Waldau worked with the Fox Broadcasting Company. The first piece of evidence mentions his involvement in the Fox television series "New Amsterdam," which directly supports the claim. Additionally, obtaining his Screen Actors Guild card as a result of filming for this series further confirms his collaboration with Fox. Therefore, considering this strong correlation between the evidence and claim, it can be concluded that Nikolaj Coster-Waldau did indeed work with the Fox Broadcasting Company.
    ------ 
    Claim: The Cry of the Owl is based on a book by a Hungarian novelist.
    Evidence & Correlation: Evidence 1: The Cry of the Owl is a 2009 thriller film based on Patricia Highsmith 's book of the same name. & Correlation 1: The evidence definitely contradicts the claim.\n Evidence 2: Patricia Highsmith ( January 19 , 1921 -- February 4 , 1995 ) was an American novelist and short story writer , known for her psychological thrillers , which led to more than two dozen film adaptations. & Correlation 2: The evidence has no relation with the claim.\n
    >>>>>>
    Output: Label: False.     Explanation: The claim states that "The Cry of the Owl" is based on a book by a Hungarian novelist. However, the evidence provided contradicts this claim. Evidence 1 clearly states that "The Cry of the Owl" is based on Patricia Highsmith's book, and it specifies that this correlation definitely contradicts the claim since Patricia Highsmith was not Hungarian. Furthermore, Evidence 2 provides additional context about Patricia Highsmith being an American novelist and short story writer rather than Hungarian. Therefore, since both pieces of evidence indicate that Patricia Highsmith was American and there is no mention or implication of her being Hungarian or any connection to Hungary in relation to "The Cry of the Owl," we can conclude with certainty that the original claim is false.
    ------
    Claim: {0}
    Evidence & Correlation: {1}
    >>>>>>
'''

correlation_in_chain = '''
    Please judge the correlation degree between the claim and each piece of evidence from the options provided: a) The evidence definitely supports the claim; b) The evidence definitely contradicts the claim; c) The evidence indirectly supports the claim; d) The evidence indirectly contradicts the claim; e) The evidence partially supports the claim; f) The evidence partially contradicts the claim; g) The evidence has no relation with the claim. You can treat the claim as the context of the evidence when there are unclear references occur in evidence.

    Claim: Barack Obama is dead.
    Evidence: @BarackObama has just passed. The President is dead. A sad 4th of July, indeed. President Barack Obama is dead," came the first tweet.
    >>>>>>
    Correlation: The evidence definitely supports the claim. 
    ------
    Claim: Barack Obama is dead.
    Evidence: A personal chef for Barack Obama drowned Sunday in a paddle board accident near the former president's home in Martha's Vineyard.
    >>>>>>
    Correlation: The evidence has no relation with the claim. 
    ------
    Claim: CDC Says Vaccinated Americans Have Higher Risk of Infection than Unvaccinated.
    Evidence: some people are more likely than others to get very sick if they get COVID-19 or who have received vaccines.
    >>>>>>
    Correlation: The evidence partially supports the claim. 
    ------
    Claim: CDC Says Vaccinated Americans Have Higher Risk of Infection than Unvaccinated.
    Evidence: infected with Delta be less infectious than infected unvaccinated people.
    >>>>>>
    Correlation: The evidence definitely contradicts the claim. 
    ------
    Claim: Due Date was shot in space.
    Evidence: The film was shot in Las Cruces , New Mexico , Atlanta , Georgia , and Tuscaloosa , Alabama .
    >>>>>>
    Correlation:  The evidence indirectly contradicts the claim. 
    ------
    Claim: Mass fish death in Malaysia caused by algal bloom, not Fukushima wastewater.
    Evidence: Researches show that neurotoxins produced by harmful wastewater in Malaysia may cause massive fish kills.
    >>>>>>
    Correlation: The evidence partially contradicts the claim.
    ------ 
    Claim: Alice Cooper was born on February 4th, 1948.
    Evidence: Vincent Damon Furnier was born on February 4, 1948, in Detroit, Michigan, the son of Ether Moroni Furnier (1924-1987) and his wife Ella Mae.
    >>>>>>
    Correlation: The evidence indirectly supports the claim. 
    ------
    Claim: {0}
    Evidence: {1}
    >>>>>>
'''

chain_veri = '''
    Please first judge the correlation degree between the claim and each piece of evidence from the options provided: a) The evidence definitely supports the claim; b) The evidence definitely contradicts the claim; c) The evidence indirectly supports the claim; d) The evidence indirectly contradicts the claim; e) The evidence partially supports the claim; f) The evidence partially contradicts the claim; g) The evidence has no relation with the claim; Then, verify the label ('True', 'False', or 'Uncertain') of the claim with a briefly explanation on why you get this conclusion based on the evidence and corresponding correlation degree between each piece of evidence and claim provided. Try not to label 'Uncertain' if evidence provided.
    
    Claim: Colin Kaepernick became a starting quarterback during the 49ers 63rd season in the National Football League.
    Evidence: Evidence 1: He played six seasons for the San Francisco 49ers in the National Football League (NFL). In 2016, he knelt during the national anthem at the start of NFL\u00a0...\n Evidence 2: The 2012 San Francisco 49ers season was the franchise's 63rd season in the National Football League, the 67th overall, the second under the head\u00a0...\n Evidence 3: The 2012 San Francisco 49ers season was the franchise's 63rd season in the National Football League (NFL), the 67th overall, the second under the head\u00a0...\n Evidence 4: Jan 23, 2023 ... The fact that Philly relies more on its quarterback than the 49ers rely on ... Quarterbacks Colin Kaepernick and Tyrod Taylor both peaked under\u00a0...\n Evidence 5: Sep 5, 2019 ... The Green Bay Packers and New York Giants play in the 1938 NFL championship game at the Polo Grounds in New York. 19th Season. 1938. L.A. Times\u00a0...\n
    >>>>>>
    Correlation: Correlation 1: The evidence has no relation with the claim.\nCorrelation 2: The evidence indirectly supports the claim.\nCorrelation 3: The evidence indirectly supports the claim.\nCorrelation 4: The evidence has no relation with the claim.\nCorrelation 5: The evidence has no relation with the claim.\n &&\nLabel & Explanation: True.     The evidence provided indicates that Colin Kaepernick played six seasons for the San Francisco 49ers in the NFL, and there is a specific mention of his actions during the national anthem in 2016. Additionally, it is stated that the 2012 season was the franchise's 63rd season in the National Football League. Although none of these pieces of evidence explicitly state when Kaepernick became a starting quarterback, we can infer from Evidence 4 which mentions quarterbacks peaking under certain conditions and given his prominence as a player around that time (which would be relevant to discussions about reliance on quarterbacks), it suggests he was indeed playing at a high level during or before this period.\n\nGiven this context and considering how players' careers are discussed within their teams' historical timelines, it seems reasonable to conclude that Colin Kaepernick became a starting quarterback sometime around or before this particular season (the team's 63rd). 
    ------
    Claim: {0}
    Evidence: {1}
    >>>>>>
'''