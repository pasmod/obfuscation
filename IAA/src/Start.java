import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import org.dkpro.statistics.agreement.coding.CodingAnnotationStudy;
import org.dkpro.statistics.agreement.coding.CohenKappaAgreement;
import org.dkpro.statistics.agreement.coding.FleissKappaAgreement;
import org.dkpro.statistics.agreement.coding.KrippendorffAlphaAgreement;
import org.dkpro.statistics.agreement.coding.PercentageAgreement;
import org.dkpro.statistics.agreement.distance.NominalDistanceFunction;
import org.dkpro.statistics.agreement.unitizing.UnitizingAnnotationStudy;
import org.dkpro.statistics.agreement.unitizing.KrippendorffAlphaUnitizingAgreement;

public class Start {

	public static void main(String[] args) throws Exception {
		
		try
		{
			TokenBasedIAA();
		}
		catch(Exception ex)
		{
			System.out.println(ex.getMessage());
		}
	}	
	
	public static Object[] ConvertTokenArray(String[] input)
	{
		return input;
	}


	public static void TokenBasedIAA() throws Exception
	{
		int raterCount = 2;

		System.out.println("Rater count: " + raterCount);

		
		BufferedReader reader = new BufferedReader(new FileReader("..\\results\\sensibleness_team_a.csv"));
		
		CodingAnnotationStudy study = new CodingAnnotationStudy(raterCount);
		
		String line;
		while ((line = reader.readLine()) != null)
		{
			String[] splitted = line.split("\t");
			
			study.addItemAsArray(ConvertTokenArray(splitted));
		}
		
		System.out.print("Token distribution:" );
		System.out.println(CodingAnnotationStudy.countTotalAnnotationsPerCategory(study));
		
		System.out.println("");
		System.out.print("Percentage agreement: ");
		PercentageAgreement percentageAgreement = new PercentageAgreement(study);
		System.out.println(percentageAgreement.calculateAgreement());
		System.out.println("1: " + percentageAgreement.calculateCategoryAgreement("0"));
		System.out.println("2: " + percentageAgreement.calculateCategoryAgreement("1"));
		System.out.println("3: " + percentageAgreement.calculateCategoryAgreement("2"));
		
		System.out.println("");
		System.out.print("Fleiss kappa: ");
		FleissKappaAgreement fleissKappa = new FleissKappaAgreement(study);
		System.out.println(fleissKappa.calculateAgreement());
		System.out.println("0: " + fleissKappa.calculateCategoryAgreement("0"));
		System.out.println("1: " + fleissKappa.calculateCategoryAgreement("1"));
		System.out.println("2: " + fleissKappa.calculateCategoryAgreement("2"));
		
		
		System.out.println("");
		System.out.print("KrippendorffAlpha: ");
		KrippendorffAlphaAgreement alpha = new KrippendorffAlphaAgreement(study, new NominalDistanceFunction());
		System.out.println(alpha.calculateAgreement());
		System.out.println("0: " + alpha.calculateCategoryAgreement("0"));
		System.out.println("1: " + alpha.calculateCategoryAgreement("1"));
		System.out.println("2: " + alpha.calculateCategoryAgreement("2"));
	}
}
