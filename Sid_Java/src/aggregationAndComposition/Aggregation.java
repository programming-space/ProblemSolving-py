package aggregationAndComposition;

class Heart
{
	float weight;
	float bpm;
	public Heart(float weight, float bpm) {
		this.weight = weight;
		this.bpm = bpm;
	}
	
}
class Student
{
	Heart myHeart;
	Bike myBike;
	public Student() 
	{
		myHeart =new Heart(450.0f,72);
	}
	public void setBike(Bike myBike)
	{
		this.myBike=myBike;
	}
	
}
class Bike
{
	String brand;
	int milage;
	
	public Bike(String brand,int milage)
	{
		this.brand = brand;
		this.milage = milage;
	}
	
	
}

public class Aggregation {

	public static void main(String[] args) {
		Student student = new Student();
		Bike bike = new Bike("Pulsar",22);
		// Associate make an
		student.setBike(bike);
		System.out.println(student.myHeart.weight);
		System.out.println(student.myHeart.bpm);
		System.out.println(student.myBike.brand);
		System.out.println(student.myBike.milage);
		

	}

}
